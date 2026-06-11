const FINAL_BLUEPRINT_STORAGE_KEY = 'bio_final_blueprint_2026_state_v1';
let blueprintRuntime = { view: 'home', trackId: null, topicId: null, drill: null, simulation: null };

function defaultBlueprintState() {
  return {
    version: 1,
    topics: {},
    openResponses: {},
    drillHistory: [],
    simulationHistory: [],
    planDone: {},
    lastOpened: null
  };
}

function loadBlueprintState() {
  try {
    return Object.assign(defaultBlueprintState(), JSON.parse(localStorage.getItem(FINAL_BLUEPRINT_STORAGE_KEY) || '{}'));
  } catch (error) {
    return defaultBlueprintState();
  }
}

function saveBlueprintState(state) {
  localStorage.setItem('bio_final_blueprint_2026_state_v1', JSON.stringify(state));
}

function blueprintState() {
  return loadBlueprintState();
}

function blueprintEscape(value) {
  return String(value == null ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function blueprintAllTopics() {
  return (FINAL_BLUEPRINT_CONTENT.tracks || []).flatMap(track =>
    (track.topics || []).map(topic => Object.assign({ trackId: track.id }, topic))
  );
}

function blueprintOpenCategories() {
  return FINAL_BLUEPRINT_CONTENT.openResponses ||
    (FINAL_BLUEPRINT_CONTENT.part4 && FINAL_BLUEPRINT_CONTENT.part4.categories) || [];
}

function blueprintTopicLessons(topic) {
  if (topic.lessons) return topic.lessons;
  return (topic.lessonRefs || []).map(reference => reference.lesson).filter(Boolean);
}

function blueprintTopicSections(topic) {
  return topic.sections || topic.sectionMappings || [];
}

function blueprintTrackDescription(track) {
  if (track.description || track.purpose) return track.description || track.purpose;
  if (track.id === 'part2') return 'Learn every teacher-listed concept from cytology, molecular genetics, heredity, evolution, and diversity of life.';
  if (track.id === 'part3') return 'Learn every teacher-listed concept from plant systems, animal systems, ecology, photosynthesis, and respiration.';
  if (track.id === 'part4') return 'Train one A/B response for each of the six required categories using a concrete 4 / 2 / 0 checklist.';
  return '';
}

function blueprintTopicById(topicId) {
  return blueprintAllTopics().find(topic => topic.id === topicId);
}

function blueprintTrackById(trackId) {
  return (FINAL_BLUEPRINT_CONTENT.tracks || []).find(track => track.id === trackId);
}

function blueprintTopicScore(topic, state) {
  const record = state.topics[topic.id] || {};
  const learned = record.learned ? 30 : 0;
  const recall = Math.min(40, (record.recallCorrect || 0) * 10);
  const drill = record.drillAttempts ? Math.round((record.drillCorrect / record.drillAttempts) * 30) : 0;
  return Math.min(100, learned + recall + drill);
}

function blueprintTrackScore(track, state) {
  if (track.id === 'part1') {
    let complete = 0;
    let total = 0;
    Object.keys(ACTIVE_RECALL_DATA || {}).forEach(unit => {
      const pages = ACTIVE_RECALL_DATA[unit] || [];
      total += pages.length;
      pages.forEach(page => {
        if (!page.questions.length || page.questions.every((question, index) => savedRecallAnswer(page, index)?.locked)) complete++;
      });
    });
    return total ? Math.round((complete / total) * 100) : 0;
  }
  if (track.id === 'part4') {
    const scores = blueprintOpenCategories().map(category =>
      Number((state.openResponses[category.id] || {}).score || 0) / 4
    );
    return scores.length ? Math.round((scores.reduce((sum, score) => sum + score, 0) / scores.length) * 100) : 0;
  }
  const topics = track.topics || [];
  return topics.length
    ? Math.round(topics.reduce((sum, topic) => sum + blueprintTopicScore(topic, state), 0) / topics.length)
    : 0;
}

function calculateBlueprintReadiness() {
  const state = blueprintState();
  const scores = {};
  (FINAL_BLUEPRINT_CONTENT.tracks || []).forEach(track => {
    scores[track.id] = blueprintTrackScore(track, state);
  });
  const weighted = Math.round(
    (scores.part1 || 0) * 0.20 +
    (scores.part2 || 0) * 0.30 +
    (scores.part3 || 0) * 0.26 +
    (scores.part4 || 0) * 0.24
  );
  const evidence = blueprintAllTopics().filter(topic => blueprintTopicScore(topic, state) > 0).length;
  return { weighted, scores, evidence, totalTopics: blueprintAllTopics().length };
}

function renderFinalBlueprint(container) {
  blueprintRuntime.view = 'home';
  const state = blueprintState();
  state.lastOpened = new Date().toISOString();
  saveBlueprintState(state);
  const readiness = calculateBlueprintReadiness();
  const today = blueprintTodayPlan();

  container.innerHTML = `
    <div class="blueprint-shell">
      <section class="blueprint-hero">
        <div>
          <div class="hero-eyebrow">Thursday, June 18, 2026 - Teacher Outline Mode</div>
          <h1>Learn the Final Before You Simulate It</h1>
          <p>This room teaches every item named on the review outline, forces closed-book retrieval, and only then sends you into exam-format practice. It is separate from all existing progress.</p>
        </div>
        <div class="blueprint-readiness" aria-label="Weighted exam readiness">
          <strong>${readiness.weighted}%</strong>
          <span>weighted readiness</span>
          <small>${readiness.evidence}/${readiness.totalTopics} focused topics have evidence</small>
        </div>
      </section>

      <section class="blueprint-today">
        <div>
          <span class="blueprint-kicker">Today's assignment</span>
          <h2>${blueprintEscape(today.title)}</h2>
          <p>${blueprintEscape(today.description)}</p>
        </div>
        <button class="q-btn primary" onclick="${today.action}">${blueprintEscape(today.button)}</button>
      </section>

      <div class="blueprint-track-grid">
        ${(FINAL_BLUEPRINT_CONTENT.tracks || []).map(track => blueprintTrackCard(track, readiness.scores[track.id] || 0)).join('')}
      </div>

      ${renderBlueprintPlan()}

      <section class="blueprint-simulation-callout">
        <div>
          <span class="blueprint-kicker">Final checkpoint</span>
          <h2>Exact-format practice</h2>
          <p>After learning, practice 20 Multiple Choice, 26 Multiple Choice, 25 Multiple Choice, and Choose A or B for each open-ended category.</p>
        </div>
        <button class="exam-btn" onclick="startBlueprintSimulation()">Start Blueprint Simulation</button>
      </section>
    </div>`;
}

function blueprintTrackCard(track, score) {
  const labels = {
    part1: 'Part 1: General Knowledge',
    part2: 'Part 2: Units 3-6',
    part3: 'Part 3: Units 7-8',
    part4: 'Part 4: Open-Ended'
  };
  const actions = track.id === 'part4'
    ? `renderBlueprintOpenResponse()`
    : `renderBlueprintTrack('${track.id}')`;
  return `
    <article class="blueprint-track-card blueprint-${track.id}">
      <div class="blueprint-track-topline">
      <span>${blueprintEscape(track.examLabel || track.format)}</span>
        <strong>${score}%</strong>
      </div>
      <h2>${labels[track.id]}</h2>
      <p>${blueprintEscape(blueprintTrackDescription(track))}</p>
      <div class="blueprint-meter"><span style="width:${score}%"></span></div>
      <button class="q-btn primary" onclick="${actions}">${blueprintEscape(track.buttonLabel || 'Open study track')}</button>
    </article>`;
}

function renderBlueprintTrack(trackId) {
  const container = document.getElementById('main-view');
  const track = blueprintTrackById(trackId);
  if (!track) return renderFinalBlueprint(container);
  blueprintRuntime = { view: 'track', trackId, topicId: null, drill: null, simulation: null };
  const state = blueprintState();

  if (trackId === 'part1') {
    container.innerHTML = `
      <div class="blueprint-shell">
        ${blueprintBackBar('Final Blueprint', "showView('final-blueprint-2026')")}
        <section class="blueprint-track-header">
          <span class="blueprint-kicker">Part 1 - 20% of exam</span>
          <h1>Part 1: General Knowledge</h1>
          <p>Part 1 can sample any idea from Units 1-8. Your existing 1,025-page Active Recall system is the complete-information source, so this track turns it into a coverage checklist instead of duplicating it.</p>
        </section>
        <div class="blueprint-unit-grid">
          ${(track.unitMappings || []).map(unit => {
            const stats = recallUnitStats(unit.unit);
            const percent = stats.total ? Math.round((stats.completed / stats.total) * 100) : 0;
            return `<article class="blueprint-unit-card">
              <span>Unit ${unit.unit}</span>
              <h3>${blueprintEscape(unit.title)}</h3>
              <p>${blueprintEscape(unit.focus)}</p>
              <div class="blueprint-meter"><span style="width:${percent}%"></span></div>
              <small>${stats.completed}/${stats.total} pages recalled</small>
              <button class="q-btn primary" onclick="openBlueprintActiveRecall(${unit.unit}, '')">Continue Active Recall</button>
            </article>`;
          }).join('')}
        </div>
        <section class="blueprint-action-row">
          <button class="exam-btn" onclick="startBlueprintDrill('part1')">20-question breadth check</button>
          <button class="q-btn" onclick="showView('active-recall')">Open full Active Recall reader</button>
        </section>
      </div>`;
    return;
  }

  const topics = track.topics || [];
  container.innerHTML = `
    <div class="blueprint-shell">
      ${blueprintBackBar('Final Blueprint', "showView('final-blueprint-2026')")}
      <section class="blueprint-track-header">
        <span class="blueprint-kicker">${blueprintEscape(track.examLabel || track.format)}</span>
        <h1>${blueprintEscape(track.title)}</h1>
        <p>${blueprintEscape(blueprintTrackDescription(track))}</p>
        <div class="blueprint-action-row">
          <button class="exam-btn" onclick="startBlueprintDrill('${trackId}')">Start adaptive mixed drill</button>
          <button class="q-btn" onclick="startBlueprintRecall('${trackId}')">Closed-book recall session</button>
        </div>
      </section>
      <nav class="blueprint-topic-nav" aria-label="Outline topics">
        ${[...new Set(topics.map(topic => `Unit ${topic.unit}`))].map(unit =>
          `<a href="#blueprint-${unit.replace(/\s/g, '-')}">${unit}</a>`
        ).join('')}
      </nav>
      <div class="blueprint-topic-list">
        ${topics.map((topic, index) => {
          const score = blueprintTopicScore(topic, state);
          const previousUnit = index ? topics[index - 1].unit : null;
          return `${previousUnit !== topic.unit ? `<h2 id="blueprint-Unit-${topic.unit}">Unit ${topic.unit}</h2>` : ''}
            <article class="blueprint-topic-row">
              <div class="blueprint-topic-score">${score}%</div>
              <div>
                <span class="blueprint-topic-meta">${blueprintEscape(blueprintTopicLessons(topic).join(', '))}</span>
                <h3>${blueprintEscape(topic.title)}</h3>
                <p>${blueprintEscape(topic.mustKnow && topic.mustKnow[0] ? topic.mustKnow[0] : topic.summary || '')}</p>
              </div>
              <button class="q-btn primary" onclick="renderBlueprintTopic('${topic.id}')">Learn and recall</button>
            </article>`;
        }).join('')}
      </div>
    </div>`;
}

function blueprintBackBar(label, action) {
  return `<div class="blueprint-backbar"><button class="q-btn" onclick="${action}">Back to ${blueprintEscape(label)}</button></div>`;
}

function renderBlueprintTopic(topicId) {
  const container = document.getElementById('main-view');
  const topic = blueprintTopicById(topicId);
  if (!topic) return;
  blueprintRuntime = { view: 'topic', trackId: topic.trackId, topicId, drill: null, simulation: null };
  const state = blueprintState();
  const record = state.topics[topicId] || {};

  container.innerHTML = `
    <div class="blueprint-shell blueprint-topic-page">
      ${blueprintBackBar(blueprintTrackById(topic.trackId).title, `renderBlueprintTrack('${topic.trackId}')`)}
      <section class="blueprint-topic-hero">
        <span class="blueprint-kicker">Unit ${topic.unit} - ${blueprintTopicLessons(topic).join(', ')}</span>
        <h1>${blueprintEscape(topic.title)}</h1>
        <p>Read this once for understanding. Then close the notes and complete the recall prompts below.</p>
        <div class="blueprint-action-row">
          ${blueprintTopicLessons(topic).map(lesson => `<button class="q-btn" onclick="openBlueprintActiveRecall(${topic.unit}, '${blueprintEscape(lesson)}')">Open ${blueprintEscape(lesson)} notes</button>`).join('')}
        </div>
      </section>

      <section class="blueprint-study-sheet">
        <div class="blueprint-kicker">Everything the outline expects you to know</div>
        <ul>${(topic.mustKnow || []).map(point => `<li>${blueprintEscape(point)}</li>`).join('')}</ul>
        ${topic.commonTrap ? `<aside><strong>Common trap:</strong> ${blueprintEscape(topic.commonTrap)}</aside>` : ''}
        <button class="q-btn primary" onclick="markBlueprintLearned('${topic.id}')">${record.learned ? 'Reviewed - read again if needed' : 'I have read and understood this'}</button>
      </section>

      <section class="blueprint-recall-sheet">
        <div class="blueprint-kicker">Closed-book retrieval</div>
        <h2>Explain these without looking above</h2>
        ${(topic.recall || []).map((item, index) => `
          <article class="blueprint-recall-card">
            <h3>${index + 1}. ${blueprintEscape(item.prompt)}</h3>
            <textarea id="blueprint-recall-${index}" placeholder="Type what you remember before revealing the answer."></textarea>
            <details>
              <summary>Reveal required answer</summary>
              <p>${blueprintEscape(item.answer)}</p>
            </details>
            <div class="blueprint-rating">
              <button class="q-btn" onclick="gradeBlueprintRecall('${topic.id}', ${index}, false)">Again</button>
              <button class="q-btn primary" onclick="gradeBlueprintRecall('${topic.id}', ${index}, true)">Got it without notes</button>
            </div>
          </article>`).join('')}
      </section>

      <section class="blueprint-action-row blueprint-topic-footer">
        <button class="exam-btn" onclick="startBlueprintDrill('${topic.trackId}', '${topic.id}')">Practice exam questions for this topic</button>
        <button class="q-btn" onclick="renderBlueprintTrack('${topic.trackId}')">Return to topic list</button>
      </section>
    </div>`;
}

function markBlueprintLearned(topicId) {
  const state = blueprintState();
  state.topics[topicId] = state.topics[topicId] || {};
  state.topics[topicId].learned = true;
  state.topics[topicId].lastStudied = Date.now();
  saveBlueprintState(state);
  renderBlueprintTopic(topicId);
}

function startBlueprintRecall(trackId) {
  const track = blueprintTrackById(trackId);
  if (!track || !(track.topics || []).length) return;
  const state = blueprintState();
  const ordered = [...track.topics].sort((a, b) => blueprintTopicScore(a, state) - blueprintTopicScore(b, state));
  renderBlueprintTopic(ordered[0].id);
}

function gradeBlueprintRecall(topicId, promptIndex, correct) {
  const state = blueprintState();
  const record = state.topics[topicId] = state.topics[topicId] || {};
  record.recallAttempts = (record.recallAttempts || 0) + 1;
  if (correct) record.recallCorrect = (record.recallCorrect || 0) + 1;
  else record.recallCorrect = Math.max(0, (record.recallCorrect || 0) - 1);
  record.lastStudied = Date.now();
  record.lastRecallPrompt = promptIndex;
  saveBlueprintState(state);
  const button = event && event.currentTarget;
  if (button) {
    button.textContent = correct ? 'Recorded: recalled' : 'Queued for review';
    button.disabled = true;
  }
}

function openBlueprintActiveRecall(unit, lesson) {
  recallState.unit = Number(unit);
  const pages = ACTIVE_RECALL_DATA[unit] || [];
  if (lesson) {
    const lessonNumber = String(lesson).match(/\d+\.\d+/);
    const normalized = lessonNumber ? `Unit_${lessonNumber[0].replace('.', '_')}` : String(lesson).replace(/\s/g, '_');
    const found = pages.findIndex(page => String(page.filename || '').replace(/\./g, '_').includes(normalized));
    if (found >= 0) recallState.page = found;
  }
  saveRecallState();
  showView('active-recall');
}

function blueprintQuestionsFor(trackId, topicId) {
  let entries = [];
  Object.keys(QUIZ_DATA || {}).forEach(unit => {
    (QUIZ_DATA[unit] || []).forEach((question, index) => {
      if (question.t && question.t !== 'mc') return;
      entries.push({ question, unit: Number(unit), index });
    });
  });
  const topic = topicId ? blueprintTopicById(topicId) : null;
  if (topic) {
    const sections = blueprintTopicSections(topic)
      .map(section => String(section).match(/\d+\.\d+/))
      .filter(Boolean)
      .map(match => match[0]);
    const sectionEntries = entries.filter(entry => sections.includes(entry.question.section));
    entries = sectionEntries.length ? sectionEntries : entries.filter(entry => entry.unit === Number(topic.unit));
    const stopWords = new Set(['and', 'the', 'for', 'with', 'from', 'into', 'that', 'this', 'are', 'cell', 'cells', 'unit']);
    const keywords = `${topic.title} ${(topic.mustKnow || []).join(' ')}`
      .toLowerCase()
      .match(/[a-z0-9]+/g)
      .filter(word => word.length > 3 && !stopWords.has(word));
    entries = entries
      .map(entry => {
        const haystack = `${entry.question.q} ${(entry.question.opts || []).join(' ')}`.toLowerCase();
        const score = keywords.reduce((total, keyword) => total + (haystack.includes(keyword) ? 1 : 0), 0);
        return Object.assign({ topicScore: score, tieBreaker: Math.random() }, entry);
      })
      .sort((a, b) => b.topicScore - a.topicScore || a.tieBreaker - b.tieBreaker);
  } else if (trackId === 'part2') {
    entries = entries.filter(entry => entry.unit >= 3 && entry.unit <= 6);
  } else if (trackId === 'part3') {
    entries = entries.filter(entry => entry.unit >= 7 && entry.unit <= 8);
  }
  return topic ? entries : shuffleArray(entries);
}

function startBlueprintDrill(trackId, topicId) {
  const pool = blueprintQuestionsFor(trackId, topicId);
  const count = topicId ? Math.min(8, pool.length) : Math.min(trackId === 'part1' ? 20 : 15, pool.length);
  blueprintRuntime.drill = {
    trackId,
    topicId: topicId || null,
    questions: pool.slice(0, count),
    index: 0,
    correct: 0,
    answers: []
  };
  renderBlueprintDrill();
}

function renderBlueprintDrill() {
  const container = document.getElementById('main-view');
  const drill = blueprintRuntime.drill;
  if (!drill || drill.index >= drill.questions.length) return finishBlueprintDrill();
  const entry = drill.questions[drill.index];
  const question = entry.question;
  container.innerHTML = `
    <div class="blueprint-shell blueprint-drill">
      ${blueprintBackBar('study track', drill.topicId ? `renderBlueprintTopic('${drill.topicId}')` : `renderBlueprintTrack('${drill.trackId}')`)}
      <section class="blueprint-drill-header">
        <span class="blueprint-kicker">Question ${drill.index + 1} of ${drill.questions.length}</span>
        <div class="blueprint-meter"><span style="width:${Math.round((drill.index / drill.questions.length) * 100)}%"></span></div>
      </section>
      <article class="blueprint-drill-card">
        <span class="blueprint-topic-meta">Unit ${entry.unit} - Lesson ${blueprintEscape(question.section)}</span>
        <h2>${blueprintEscape(question.q)}</h2>
        <div class="blueprint-drill-options">
          ${(question.opts || []).map((option, index) =>
            `<button onclick="answerBlueprintDrill(${index})"><span>${String.fromCharCode(65 + index)}</span>${blueprintEscape(option)}</button>`
          ).join('')}
        </div>
        <div id="blueprint-drill-feedback"></div>
      </article>
    </div>`;
}

function answerBlueprintDrill(answerIndex) {
  const drill = blueprintRuntime.drill;
  const entry = drill.questions[drill.index];
  const question = entry.question;
  const correctIndex = Number(question.a);
  const correct = answerIndex === correctIndex;
  if (correct) drill.correct++;
  drill.answers.push({ section: question.section, correct });

  const feedback = document.getElementById('blueprint-drill-feedback');
  const explanation = question.exp || (question.explanations && question.explanations[correctIndex]) || '';
  feedback.className = `blueprint-drill-feedback ${correct ? 'correct' : 'wrong'}`;
  feedback.innerHTML = `<strong>${correct ? 'Correct' : `Correct answer: ${String.fromCharCode(65 + correctIndex)}`}</strong><p>${blueprintEscape(explanation)}</p><button class="q-btn primary" onclick="nextBlueprintDrillQuestion()">Next question</button>`;
  document.querySelectorAll('.blueprint-drill-options button').forEach((button, index) => {
    button.disabled = true;
    if (index === correctIndex) button.classList.add('correct');
    else if (index === answerIndex) button.classList.add('wrong');
  });
}

function nextBlueprintDrillQuestion() {
  blueprintRuntime.drill.index++;
  renderBlueprintDrill();
}

function finishBlueprintDrill() {
  const container = document.getElementById('main-view');
  const drill = blueprintRuntime.drill;
  if (!drill) return;
  const state = blueprintState();
  if (drill.topicId) {
    const record = state.topics[drill.topicId] = state.topics[drill.topicId] || {};
    record.drillAttempts = (record.drillAttempts || 0) + drill.questions.length;
    record.drillCorrect = (record.drillCorrect || 0) + drill.correct;
    record.lastStudied = Date.now();
  }
  state.drillHistory.push({
    date: new Date().toISOString(),
    trackId: drill.trackId,
    topicId: drill.topicId,
    correct: drill.correct,
    total: drill.questions.length,
    misses: drill.answers.filter(answer => !answer.correct).map(answer => answer.section)
  });
  state.drillHistory = state.drillHistory.slice(-50);
  saveBlueprintState(state);
  const percent = drill.questions.length ? Math.round((drill.correct / drill.questions.length) * 100) : 0;
  container.innerHTML = `
    <div class="blueprint-shell">
      <section class="blueprint-finish-card">
        <span class="blueprint-kicker">Retrieval round complete</span>
        <h1>${drill.correct}/${drill.questions.length} correct</h1>
        <p>${percent >= 85 ? 'Strong retrieval. Review the explanations you missed, then move forward.' : 'This is useful evidence, not failure. Relearn the missed ideas and repeat the drill tomorrow.'}</p>
        <div class="blueprint-action-row">
          <button class="exam-btn" onclick="startBlueprintDrill('${drill.trackId}'${drill.topicId ? `, '${drill.topicId}'` : ''})">Practice again</button>
          <button class="q-btn" onclick="${drill.topicId ? `renderBlueprintTopic('${drill.topicId}')` : `renderBlueprintTrack('${drill.trackId}')`}">Return to study</button>
        </div>
      </section>
    </div>`;
}

function renderBlueprintOpenResponse(categoryId) {
  const container = document.getElementById('main-view');
  const categories = blueprintOpenCategories();
  const category = categories.find(item => item.id === categoryId) || categories[0];
  if (!category) return;
  blueprintRuntime = { view: 'open', trackId: 'part4', topicId: category.id, drill: null, simulation: null };
  const state = blueprintState();
  const saved = state.openResponses[category.id] || { option: 'A', text: '', checklist: {}, score: 0 };
  const prompt = category.prompts.find(item => item.option === saved.option) || category.prompts[0];

  container.innerHTML = `
    <div class="blueprint-shell">
      ${blueprintBackBar('Final Blueprint', "showView('final-blueprint-2026')")}
      <section class="blueprint-track-header">
        <span class="blueprint-kicker">Part 4 - 24% of exam - answer six responses</span>
        <h1>Part 4: Open-Ended</h1>
        <p>Choose A or B for each category. Train by outlining from memory, writing a complete response, and checking every required biological connection.</p>
      </section>
      <nav class="blueprint-open-tabs">
        ${categories.map(item => `<button class="${item.id === category.id ? 'active' : ''}" onclick="renderBlueprintOpenResponse('${item.id}')">${blueprintEscape(item.title)}</button>`).join('')}
      </nav>
      <section class="blueprint-open-card">
        <div class="blueprint-open-choice">
          ${category.prompts.map(item => `<button class="${item.option === saved.option ? 'active' : ''}" onclick="selectBlueprintOpenOption('${category.id}', '${item.option}')">Option ${item.option}: ${blueprintEscape(item.title)}</button>`).join('')}
        </div>
        <h2>${blueprintEscape(category.title)} - Option ${prompt.option}</h2>
        <p class="blueprint-open-prompt">${blueprintEscape(prompt.prompt)}</p>
        <div class="blueprint-action-row">
          <button class="q-btn" onclick="openBlueprintActiveRecall(${(category.units || [category.unit])[0]}, '')">Open Unit ${(category.units || [category.unit])[0]} Active Recall</button>
        </div>
        <label class="blueprint-writing-label" for="blueprint-open-text">Write your one-page response from memory</label>
        <textarea id="blueprint-open-text" class="blueprint-open-text" oninput="saveBlueprintOpenText('${category.id}', this.value)">${blueprintEscape(saved.text || '')}</textarea>
        <div class="blueprint-open-checklist">
          <h3>Required points for a proficient response</h3>
          ${(prompt.requiredPoints || []).map((point, index) => `<label><input type="checkbox" ${saved.checklist && saved.checklist[index] ? 'checked' : ''} onchange="toggleBlueprintChecklist('${category.id}', ${index}, this.checked)"> ${blueprintEscape(point)}</label>`).join('')}
        </div>
        <details class="blueprint-rubric">
          <summary>Reveal the 4 / 2 / 0 scoring guide and model</summary>
          <p><strong>4 - Proficient:</strong> ${blueprintEscape((prompt.rubric && prompt.rubric.proficient) || category.rubric[4])}</p>
          <p><strong>2 - Partially Proficient:</strong> ${blueprintEscape((prompt.rubric && prompt.rubric.partial) || category.rubric[2])}</p>
          <p><strong>0 - Not Proficient:</strong> ${blueprintEscape((prompt.rubric && (prompt.rubric.notProficient || prompt.rubric.not_proficient)) || category.rubric[0])}</p>
          ${prompt.modelAnswer ? `<p><strong>Model response:</strong> ${blueprintEscape(prompt.modelAnswer)}</p>` : ''}
        </details>
        <div class="blueprint-self-score">
          <strong>Score only after comparing your response:</strong>
          ${[0, 2, 4].map(score => `<button class="${Number(saved.score) === score ? 'active' : ''}" onclick="scoreBlueprintOpenResponse('${category.id}', ${score})">${score} points</button>`).join('')}
        </div>
      </section>
    </div>`;
}

function selectBlueprintOpenOption(categoryId, option) {
  const state = blueprintState();
  const saved = state.openResponses[categoryId] = state.openResponses[categoryId] || {};
  saved.option = option;
  saved.text = '';
  saved.checklist = {};
  saved.score = 0;
  saveBlueprintState(state);
  renderBlueprintOpenResponse(categoryId);
}

function saveBlueprintOpenText(categoryId, text) {
  const state = blueprintState();
  const saved = state.openResponses[categoryId] = state.openResponses[categoryId] || { option: 'A', checklist: {}, score: 0 };
  saved.text = text;
  saved.updatedAt = Date.now();
  saveBlueprintState(state);
}

function toggleBlueprintChecklist(categoryId, index, checked) {
  const state = blueprintState();
  const saved = state.openResponses[categoryId] = state.openResponses[categoryId] || { option: 'A', text: '', checklist: {}, score: 0 };
  saved.checklist = saved.checklist || {};
  saved.checklist[index] = checked;
  saveBlueprintState(state);
}

function scoreBlueprintOpenResponse(categoryId, score) {
  const state = blueprintState();
  const saved = state.openResponses[categoryId] = state.openResponses[categoryId] || { option: 'A', text: '', checklist: {} };
  saved.score = Number(score);
  saved.scoredAt = Date.now();
  saveBlueprintState(state);
  renderBlueprintOpenResponse(categoryId);
}

function blueprintPlanDays() {
  return [
    {
      date: '2026-06-11',
      label: 'Thu Jun 11',
      title: 'Set the map',
      description: 'Read the teacher outline, open Part 2, and master the three weakest Unit 3 topics.',
      button: 'Study Part 2',
      action: "renderBlueprintTrack('part2')"
    },
    {
      date: '2026-06-12',
      label: 'Fri Jun 12',
      title: 'Unit 4 molecular genetics',
      description: 'Study DNA structure through biotechnology, then complete a 15-question Part 2 drill.',
      button: 'Study Part 2',
      action: "renderBlueprintTrack('part2')"
    },
    {
      date: '2026-06-13',
      label: 'Sat Jun 13',
      title: 'Heredity, evolution, and diversity',
      description: 'Finish Units 4-6 outline topics and write one Part 4 response.',
      button: 'Study Part 2',
      action: "renderBlueprintTrack('part2')"
    },
    {
      date: '2026-06-14',
      label: 'Sun Jun 14',
      title: 'Plants and animal systems',
      description: 'Master all Unit 7 outline topics, then complete one Unit 7 open response.',
      button: 'Study Part 3',
      action: "renderBlueprintTrack('part3')"
    },
    {
      date: '2026-06-15',
      label: 'Mon Jun 15',
      title: 'Ecology and cellular energy',
      description: 'Master all Unit 8 outline topics, then complete one Unit 8 open response.',
      button: 'Study Part 3',
      action: "renderBlueprintTrack('part3')"
    },
    {
      date: '2026-06-16',
      label: 'Tue Jun 16',
      title: 'Breadth and written responses',
      description: 'Use Active Recall for Parts 1 breadth and complete the remaining open-response categories.',
      button: 'Open Part 1',
      action: "renderBlueprintTrack('part1')"
    },
    {
      date: '2026-06-17',
      label: 'Wed Jun 17',
      title: 'Full exact-count simulation',
      description: 'Take one complete simulation, then relearn only the concepts you missed.',
      button: 'Start simulation',
      action: 'startBlueprintSimulation()'
    },
    {
      date: '2026-06-18',
      label: 'Thu Jun 18',
      title: 'Light recall only',
      description: 'Review equations, process order, and open-response checklists. Stop heavy studying early.',
      button: 'Open Blueprint',
      action: "renderBlueprintTrack('part2')"
    }
  ];
}

function blueprintTodayPlan() {
  const date = new Date();
  const key = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
  const plan = blueprintPlanDays().find(day => day.date === key);
  return plan || {
    title: 'Start with the weakest high-value track',
    description: 'Complete one focused topic, one closed-book recall round, and one short drill.',
    button: 'Open Part 2',
    action: "renderBlueprintTrack('part2')"
  };
}

function renderBlueprintPlan() {
  const state = blueprintState();
  return `<section class="blueprint-plan">
    <div class="blueprint-plan-heading">
      <div><span class="blueprint-kicker">June 11-18</span><h2>Your exam-week plan</h2></div>
      <p>Part 2 and Part 3 get the most time because together they are 56% of the exam.</p>
    </div>
    <div class="blueprint-plan-grid">
      ${blueprintPlanDays().map(day => `<label class="${state.planDone[day.date] ? 'done' : ''}">
        <input type="checkbox" ${state.planDone[day.date] ? 'checked' : ''} onchange="toggleBlueprintPlanDay('${day.date}', this.checked)">
        <span>${blueprintEscape(day.label)}</span>
        <strong>${blueprintEscape(day.title)}</strong>
        <small>${blueprintEscape(day.description)}</small>
      </label>`).join('')}
    </div>
  </section>`;
}

function toggleBlueprintPlanDay(date, done) {
  const state = blueprintState();
  state.planDone[date] = done;
  saveBlueprintState(state);
  renderFinalBlueprint(document.getElementById('main-view'));
}

function blueprintNormalizeQuestion(question, unit) {
  return {
    q: question.q,
    opts: [...question.opts],
    a: Number(question.a),
    explanations: question.explanations || question.opts.map((option, index) =>
      index === Number(question.a) ? (question.exp || 'This is the correct biological explanation.') : 'This choice does not match the mechanism asked about.'
    ),
    section: question.section || String(unit)
  };
}

function blueprintShuffleOptions(question) {
  const indexed = question.opts.map((text, index) => ({ text, correct: index === question.a, explanation: question.explanations[index] }));
  const shuffled = shuffleArray(indexed);
  return Object.assign({}, question, {
    opts: shuffled.map(item => item.text),
    explanations: shuffled.map(item => item.explanation),
    a: shuffled.findIndex(item => item.correct)
  });
}

function blueprintSimulationPool(minUnit, maxUnit, count) {
  const pool = [];
  Object.keys(QUIZ_DATA || {}).forEach(unit => {
    const numericUnit = Number(unit);
    if (numericUnit < minUnit || numericUnit > maxUnit) return;
    (QUIZ_DATA[unit] || []).forEach(question => {
      if (!question.t || question.t === 'mc') pool.push(blueprintShuffleOptions(blueprintNormalizeQuestion(question, numericUnit)));
    });
  });
  return shuffleArray(pool).slice(0, count);
}

function startBlueprintSimulation() {
  blueprintRuntime.simulation = {
    startedAt: Date.now(),
    parts: {
      part1: blueprintSimulationPool(1, 8, 20),
      part2: blueprintSimulationPool(3, 6, 26),
      part3: blueprintSimulationPool(7, 8, 25)
    },
    answers: { part1: {}, part2: {}, part3: {} },
    openResponses: Object.fromEntries(blueprintOpenCategories().map(category => [
      category.id,
      { option: 'A', text: '', score: 0 }
    ])),
    submitted: false
  };
  renderBlueprintSimulation();
}

function renderBlueprintSimulation() {
  const container = document.getElementById('main-view');
  const session = blueprintRuntime.simulation;
  if (!session) return renderFinalBlueprint(container);
  container.innerHTML = `
    <div class="blueprint-shell blueprint-simulation">
      ${blueprintBackBar('Final Blueprint', "showView('final-blueprint-2026')")}
      <section class="blueprint-track-header">
        <span class="blueprint-kicker">Official-format checkpoint</span>
        <h1>Biology Final Blueprint Simulation</h1>
        <p>20 Multiple Choice general questions, 26 Multiple Choice from Units 3-6, 25 Multiple Choice from Units 7-8, then Choose A or B for each of six open-ended categories.</p>
      </section>
      ${['part1', 'part2', 'part3'].map((part, partIndex) => `
        <section class="blueprint-sim-part">
          <h2>Part ${partIndex + 1}: ${part === 'part1' ? 'General Knowledge' : part === 'part2' ? 'Units 3-6' : 'Units 7-8'}</h2>
          ${session.parts[part].map((question, index) => `
            <article class="blueprint-sim-question">
              <h3>${index + 1}. ${blueprintEscape(question.q)}</h3>
              ${(question.opts || []).map((option, optionIndex) => `<label><input type="radio" name="${part}-${index}" onchange="answerBlueprintSimulation('${part}', ${index}, ${optionIndex})"> ${String.fromCharCode(65 + optionIndex)}. ${blueprintEscape(option)}</label>`).join('')}
            </article>`).join('')}
        </section>`).join('')}
      <section class="blueprint-sim-part">
        <h2>Part 4: Open-Ended</h2>
        <p>Choose A or B for each of the six categories and write the response. Afterward, compare with the trainer rubric and self-score 0, 2, or 4.</p>
        ${blueprintOpenCategories().map(category => {
          const response = session.openResponses[category.id];
          const activePrompt = category.prompts.find(prompt => prompt.option === response.option) || category.prompts[0];
          return `<article class="blueprint-sim-written">
            <h3>${blueprintEscape(category.title)}</h3>
            <div class="blueprint-open-choice">
              ${category.prompts.map(prompt => `<button type="button" class="${prompt.option === response.option ? 'active' : ''}" onclick="selectBlueprintSimulationPrompt('${category.id}', '${prompt.option}')">Option ${prompt.option}: ${blueprintEscape(prompt.title)}</button>`).join('')}
            </div>
            <p id="blueprint-sim-prompt-${category.id}" class="blueprint-open-prompt">${blueprintEscape(activePrompt.prompt)}</p>
            <textarea oninput="saveBlueprintSimulationOpenText('${category.id}', this.value)" placeholder="Write your response for ${blueprintEscape(category.title)} here.">${blueprintEscape(response.text)}</textarea>
            <label class="blueprint-sim-open-score">Self-score after rubric review
              <select onchange="scoreBlueprintSimulationOpen('${category.id}', this.value)">
                <option value="0" ${response.score === 0 ? 'selected' : ''}>0 - Not proficient</option>
                <option value="2" ${response.score === 2 ? 'selected' : ''}>2 - Partially proficient</option>
                <option value="4" ${response.score === 4 ? 'selected' : ''}>4 - Proficient</option>
              </select>
            </label>
          </article>`;
        }).join('')}
      </section>
      <button class="exam-btn blueprint-submit-sim" onclick="submitBlueprintSimulation()">Submit and calculate weighted readiness</button>
    </div>`;
}

function answerBlueprintSimulation(part, index, answer) {
  const session = blueprintRuntime.simulation;
  if (session) session.answers[part][index] = Number(answer);
}

function scoreBlueprintSimulationOpen(categoryId, score) {
  if (blueprintRuntime.simulation) blueprintRuntime.simulation.openResponses[categoryId].score = Number(score);
}

function selectBlueprintSimulationPrompt(categoryId, option) {
  const session = blueprintRuntime.simulation;
  if (!session) return;
  const response = session.openResponses[categoryId];
  response.option = option;
  const category = blueprintOpenCategories().find(item => item.id === categoryId);
  const prompt = category && category.prompts.find(item => item.option === option);
  const promptElement = document.getElementById(`blueprint-sim-prompt-${categoryId}`);
  if (promptElement && prompt) promptElement.textContent = prompt.prompt;
  const article = promptElement && promptElement.closest('.blueprint-sim-written');
  if (article) {
    article.querySelectorAll('.blueprint-open-choice button').forEach(button => {
      button.classList.toggle('active', button.textContent.trim().startsWith(`Option ${option}:`));
    });
  }
}

function saveBlueprintSimulationOpenText(categoryId, text) {
  if (blueprintRuntime.simulation) blueprintRuntime.simulation.openResponses[categoryId].text = text;
}

function submitBlueprintSimulation() {
  const session = blueprintRuntime.simulation;
  if (!session) return;
  const result = {};
  ['part1', 'part2', 'part3'].forEach(part => {
    const questions = session.parts[part];
    result[part] = questions.reduce((total, question, index) =>
      total + (session.answers[part][index] === question.a ? 1 : 0), 0
    );
  });
  const openTotal = Object.values(session.openResponses).reduce((sum, response) => sum + Number(response.score), 0);
  const weighted = Math.round(
    (result.part1 / 20) * 20 +
    (result.part2 / 26) * 30 +
    (result.part3 / 25) * 26 +
    openTotal
  );
  const state = blueprintState();
  state.simulationHistory.push({
    date: new Date().toISOString(),
    result,
    openTotal,
    weighted,
    openResponses: session.openResponses
  });
  state.simulationHistory = state.simulationHistory.slice(-10);
  saveBlueprintState(state);
  document.getElementById('main-view').innerHTML = `
    <div class="blueprint-shell">
      <section class="blueprint-finish-card">
        <span class="blueprint-kicker">Blueprint simulation complete</span>
        <h1>${weighted}% weighted score</h1>
        <p>Part 1: ${result.part1}/20 | Part 2: ${result.part2}/26 | Part 3: ${result.part3}/25 | Part 4: ${openTotal}/24</p>
        <p>This is a readiness estimate, not a guarantee. Use the lowest section to choose what you study next.</p>
        <div class="blueprint-action-row">
          <button class="exam-btn" onclick="startBlueprintSimulation()">Try another version</button>
          <button class="q-btn" onclick="showView('final-blueprint-2026')">Return to Blueprint</button>
        </div>
      </section>
    </div>`;
}
