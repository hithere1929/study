const HISTORY_OUTLINE_ITEMS = [
  ["Unit 5", "Causes of the Industrial Revolution", "Second Agricultural Revolution, enclosure, coal and iron, capital, labor, entrepreneurs, stable government, colonies, ports, and rising demand"],
  ["Unit 5", "Second Agricultural Revolution", "More productive farming through crop rotation, seed drill, selective breeding, soil improvement, and enclosure, creating food surplus and city labor"],
  ["Unit 5", "James Watt", "Improved Newcomen's steam engine with a separate condenser and rotary motion, making steam power efficient for factories and transportation"],
  ["Unit 5", "Steam engine improvements", "Powered factories, mines, railroads, and steamships; moved heavier loads farther, lowered shipping costs, and expanded markets"],
  ["Unit 5", "England as the center", "Britain had coal, iron, capital, banks, entrepreneurs, stable government, ports, colonies, markets, navy, and workers from enclosure"],
  ["Unit 5", "Outcomes of the Industrial Age", "Urbanization, factory labor, mass production, cheaper goods, new social classes, harsh conditions, pollution, reform movements, and new ideologies"],
  ["Unit 5", "Transportation Revolution", "Steam railroads, steamships, canals, and improved roads connected markets, moved goods faster, lowered costs, and increased demand"],
  ["Unit 5", "Rapid urbanization", "Fast city growth as rural workers moved to factory towns, causing overcrowding, disease, pollution, poverty, class tension, and reform pressure"],
  ["Unit 5", "Adam Smith", "Capitalism, private property, competition, division of labor, laissez-faire, free markets, invisible hand, and productive wealth beyond gold"],
  ["Unit 5", "Karl Marx", "Class conflict between bourgeoisie owners and proletariat workers; capitalism exploits labor and should be replaced by socialism or communism"],
  ["Unit 5", "City work changes", "Work shifted to factory wage labor with machines, clocks, long hours, discipline, danger, low wages, and women and child workers"],
  ["Unit 5", "Corporations and monopolies", "Shareholder-owned corporations raised capital for industry; some formed monopolies that controlled markets and reduced competition"],
  ["Unit 5", "Cult of Domesticity", "Middle- and upper-class gender ideology saying women belonged in the home as moral wives and mothers while men worked publicly"],
  ["Unit 5", "Temperance and Suffrage", "Women organized against alcohol's family harms and for voting rights, gaining public reform experience and demanding political voice"],
  ["Unit 5", "Social Darwinism and Scientific Racism", "Fake applications of survival-of-the-fittest and racial science used to justify poverty, inequality, imperialism, segregation, and hierarchy"],
  ["Unit 6", "Conservatives vs Liberals", "Conservatives defended monarchy, church, aristocracy, tradition, and order; liberals wanted constitutions, civil liberties, legal equality, and representation"],
  ["Unit 6", "Nationalism", "Loyalty to people sharing language, culture, history, ethnicity, or identity, often demanding political unity or self-rule"],
  ["Unit 6", "Congress of Vienna", "Post-Napoleon meeting restoring monarchies, redrawing borders, balancing power, containing France, and defending conservative order"],
  ["Unit 6", "French internal crises", "Unstable restored monarchies, economic problems, demands for voting rights, class conflict, revolutionary memories, and distrust of conservative rule"],
  ["Unit 6", "France's Second Republic", "Republic created after 1848; Louis-Napoleon became president, then staged a coup and ruled as Napoleon III"],
  ["Unit 6", "Toussaint L'Ouverture", "Formerly enslaved Haitian revolutionary and skilled general who organized forces, used alliances, and helped defeat French colonial power"],
  ["Unit 6", "Mexico's independence", "Revolts against Spain beginning with Hidalgo and Morelos, later completed when Creole elites backed independence under Iturbide"],
  ["Unit 6", "Simon Bolivar", "Creole revolutionary leader called the Liberator who led campaigns freeing much of northern South America from Spanish rule"],
  ["Unit 6", "German Confederation", "Loose association of German states created after Napoleon, dominated by Austria, and shaped by Metternich to preserve balance"],
  ["Unit 6", "Bismarck and Realpolitik", "Prussian leader who unified Germany; Realpolitik means practical power politics based on state interest, not moral ideals"],
  ["Unit 6", "Bismarck's actions", "Strengthened the army, used diplomacy, isolated enemies, and fought Denmark, Austria, and France to unify Germany under Prussia"],
  ["Unit 6", "William II removes Bismarck", "William II wanted personal rule and a more aggressive imperial and naval policy, so Bismarck's dominance became a threat"],
  ["Unit 6", "Cavour and Garibaldi", "Cavour used diplomacy and alliances for northern Italy; Garibaldi led Red Shirts in the south and handed lands to Victor Emmanuel II"],
  ["Unit 6", "New Italian state struggles", "Regional division, poverty, weak national identity, north-south differences, conflict with the Catholic Church, and labor or socialist tensions"],
  ["Unit 6", "Victorian Parliament", "Gradual suffrage and labor reforms, but women and many poor remained excluded for long periods and the Irish crisis continued"],
  ["Unit 6", "Suez Canal", "Mediterranean-Red Sea route shortening Europe-Asia trade; French interests helped build it and British control grew through Egyptian debt"],
  ["Unit 6", "Napoleon III deposed", "France lost the Franco-Prussian War; Napoleon III was defeated and captured at Sedan, Paris was besieged, and the empire collapsed"],
  ["Unit 6", "Paris Commune", "Radical socialist municipal government in Paris in 1871 that resisted the conservative national government after defeat by Prussia"],
  ["Unit 6", "Dreyfus and Zionism", "Jewish French army officer falsely accused of treason; antisemitism in the affair convinced Herzl Jews needed a secure homeland"],
  ["Unit 6", "Dual Monarchy", "1867 compromise gave Austria and Hungary equal status under one monarch while Slavs and other national groups remained excluded"],
  ["Unit 6", "Ottoman decline", "Nationalist revolts, Balkan losses, European pressure, debt, military weakness, weak central control, and incomplete reforms weakened the empire"],
  ["Unit 6", "Russian modernization", "Alexander II emancipated serfs, created zemstvos, and Russia expanded railroads and industry, but modernization remained uneven and autocratic"],
  ["Unit 6", "Russia before World War I", "Autocracy, poverty, worker unrest, land hunger, defeat by Japan, Bloody Sunday, weak Duma, repression, and uneven industrialization"],
  ["Unit 7", "Definition of Imperialism", "A stronger country extending political, economic, military, or cultural control over another region or people"],
  ["Unit 7", "Age of Exploration impact", "Exploration created routes, maps, ports, colonies, navigation knowledge, global rivalry, and capital that later supported imperial control"],
  ["Unit 7", "Motives of Imperialism", "Economic resources and markets, military bases, political prestige and rivalry, and ideological or missionary civilizing claims"],
  ["Unit 7", "Direct and indirect rule", "Direct rule uses foreign officials; indirect rule governs through local rulers under imperial supervision while keeping real control"],
  ["Unit 7", "Protectorate vs sphere of influence", "Protectorate keeps local government under foreign control; sphere of influence gives a foreign power special trade or investment privileges"],
  ["Unit 7", "Negative effects on Africa", "Conquest, forced labor, resource extraction, artificial borders, ethnic division, cultural disruption, economic dependence, violence, and loss of sovereignty"],
  ["Unit 7", "King Leopold II", "Belgian king who personally controlled the Congo Free State and exploited rubber and ivory through brutal forced labor and violence"],
  ["Unit 7", "Berlin Conference", "European powers set rules for claiming African territory and avoiding war among themselves; Africans were not invited"],
  ["Unit 7", "Muslim empires respond", "Selective modernization, military reform, constitutional reform, western education, and concessions, limited by debt, nationalism, and European pressure"],
  ["Unit 7", "Muhammad Ali", "Modernized Egypt through cotton production, a modern army, western-style education and training, industry, and stronger state control"],
  ["Unit 7", "Young Turks", "Ottoman reformers seeking constitutional modernization whose Turkish nationalism alienated Arabs, Armenians, and other non-Turkish peoples"],
  ["Unit 7", "Persia between Russia and England", "Persia lay between Russian expansion and British interests in India and trade routes, so both powers pressured and divided influence"],
  ["Unit 7", "Indian anger at British East India Company", "British expansion, economic exploitation, racism, missionary pressure, low pay, military rules, and disrespect for Indian religion and culture"],
  ["Unit 7", "Sepoy Rebellion cause", "Cow and pig fat cartridge rumor offended Hindu and Muslim sepoys and sparked rebellion on top of deeper resentment"],
  ["Unit 7", "Sepoy Rebellion outcomes", "The East India Company lost control; Britain established direct Crown rule, reorganized the army, tightened control, and became more cautious"],
  ["Unit 7", "Ram Mohan Roy", "Indian reformer who supported modernization, education, women's rights, ending sati, and a modern independent India"],
  ["Unit 7", "Opium War outbreak", "Britain sold illegal opium to fix trade imbalance; Qing officials tried to suppress it and Britain used the conflict to go to war"],
  ["Unit 7", "Opium War results", "China lost, signed Treaty of Nanjing, ceded Hong Kong, opened treaty ports, paid indemnities, and accepted extraterritorial privileges"],
  ["Unit 7", "China's internal and external tensions", "Unequal treaties, spheres of influence, opium pressure, foreign intervention, Taiping and Boxer rebellions, and limited reform weakened Qing rule"],
  ["Unit 7", "United States in China", "Promoted the Open Door Policy to keep China open to equal trade by all powers and protect American commercial access"],
  ["Unit 7", "Meiji Restoration", "Centralized imperial authority, ended feudal privileges, industrialized, modernized army, navy, education, and government, and made Japan imperial"],
  ["Unit 8", "MANIIA", "Militarism, Alliances, Nationalism, Industrialization, Imperialism, and Assassination: long-term causes plus the spark of World War I"],
  ["Unit 8", "Dreadnoughts", "Naval arms race ships that supported heavy industry jobs in steel, coal, shipbuilding, and weapons while increasing military tension"],
  ["Unit 8", "Franz Ferdinand assassination", "Sparked the July Crisis: Austria-Hungary blamed Serbia, issued an ultimatum, and alliances and mobilization widened the conflict"],
  ["Unit 8", "Japan takes advantage", "Japan joined the Allies, seized German holdings in China and the Pacific, and issued the Twenty-One Demands to expand influence"],
  ["Unit 8", "Sykes-Picot Treaty", "Secret British-French agreement to divide Ottoman Middle Eastern lands into spheres or mandates after the war"],
  ["Unit 8", "Russia leaves World War I", "Russian Revolution brought Lenin and Bolsheviks to power; they wanted peace to focus on internal crisis, food shortages, and revolution"],
  ["Unit 8", "United States joins World War I", "Germany resumed unrestricted submarine warfare, Zimmermann Telegram proposed a German-Mexican alliance, and U.S. trade and loans favored Allies"],
  ["Unit 8", "War end and Versailles", "Allied pressure and U.S. troops pushed Germany to armistice; Versailles blamed Germany, demanded reparations, limited military, took territory, and created League"]
];

const HISTORY_OUTLINE_DISTRACTORS = {
  "Unit 5": [
    "Restored medieval guild control, reduced private investment, and moved workers away from factories into rural cottage production",
    "Relied mainly on digital communication, automobiles, petroleum, and twentieth-century assembly lines rather than coal and steam",
    "Created immediate equality for every social class and removed pollution, poverty, dangerous labor, and political conflict",
    "Defended monarchy, church authority, aristocratic privilege, and the old order against liberal and nationalist movements",
    "Divided Africa among European powers without African representatives and justified control through imperial claims"
  ],
  "Unit 6": [
    "Expanded factory wage labor, mass production, coal power, and urban working-class life during industrialization",
    "Created spheres of influence, protectorates, direct rule, and resource extraction in Africa and Asia",
    "Explained free-market capitalism through laissez-faire, competition, private property, and the invisible hand",
    "Linked militarism, alliances, imperial rivalry, industrialized weapons, nationalism, and assassination to World War I",
    "Forced China to open treaty ports, cede Hong Kong, and accept extraterritorial rights after Britain defended opium profits"
  ],
  "Unit 7": [
    "Restored conservative monarchies after Napoleon and tried to suppress liberalism and nationalism across Europe",
    "Unified Germany through Prussian leadership, Realpolitik, army expansion, and wars against Denmark, Austria, and France",
    "Shifted Europe from rural production toward factory labor, rapid urbanization, and new industrial social classes",
    "Ended World War I with German war guilt, reparations, military limits, territorial losses, and the League of Nations",
    "Used Enlightenment ideas about natural rights, popular sovereignty, and consent to justify revolution against absolute monarchy"
  ],
  "Unit 8": [
    "Used crop rotation, enclosure, and seed drill farming to create food surplus and an industrial labor force",
    "Created nationalist unification in Germany and Italy while destabilizing multinational empires like Austria-Hungary",
    "Extended European control through direct rule, indirect rule, protectorates, spheres of influence, and forced labor systems",
    "Argued that competition and laissez-faire markets should guide production without heavy government intervention",
    "Promoted Zionism after antisemitism in the Dreyfus Affair convinced Herzl that Jews needed a secure homeland"
  ]
};

function historyOutlineRead(key, fallback) {
  try { return JSON.parse(localStorage.getItem(key) || 'null') || fallback; } catch(e) { return fallback; }
}

function historyOutlineWrite(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
  if (typeof flashSaveIndicator === 'function') flashSaveIndicator();
}

function getHistoryOutlineAnswers() {
  return historyOutlineRead('history_outline_answers_v2', {});
}

function setHistoryOutlineAnswers(answers) {
  historyOutlineWrite('history_outline_answers_v2', answers);
}

function getHistoryOutlineChoiceOrders() {
  return historyOutlineRead('history_outline_choice_orders_v2', {});
}

function setHistoryOutlineChoiceOrders(orders) {
  historyOutlineWrite('history_outline_choice_orders_v2', orders);
}

function getHistoryOutlineDistractors(unit, idx, correct) {
  const sameUnit = HISTORY_OUTLINE_ITEMS
    .map((entry, itemIdx) => ({ entry, itemIdx }))
    .filter(item => item.entry[0] === unit && item.itemIdx !== idx);
  const ranked = sameUnit
    .map(item => ({
      answer: item.entry[2],
      distance: Math.abs(item.itemIdx - idx),
      itemIdx: item.itemIdx
    }))
    .filter(item => item.answer !== correct)
    .sort((a, b) => a.distance - b.distance || a.itemIdx - b.itemIdx);

  const picked = [];
  ranked.forEach(item => {
    if (picked.length < 3 && !picked.includes(item.answer)) picked.push(item.answer);
  });

  if (picked.length < 3) {
    HISTORY_OUTLINE_ITEMS.forEach(item => {
      if (picked.length < 3 && item[2] !== correct && !picked.includes(item[2])) picked.push(item[2]);
    });
  }
  return picked;
}

function makeHistoryOutlineQuestion(item, idx) {
  const [unit, topic, correct] = item;
  const pickedWrong = getHistoryOutlineDistractors(unit, idx, correct);
  const correctSlot = (idx * 3 + 1) % 4;
  const opts = [];
  let wrongCursor = 0;
  for (let slot = 0; slot < 4; slot++) {
    opts.push(slot === correctSlot ? correct : pickedWrong[wrongCursor++]);
  }
  return {
    unit,
    topic,
    q: `Your teacher's outline asks about "${topic}." Which response would best answer that exact prompt?`,
    opts,
    a: correctSlot,
    explanation: correct
  };
}

function getHistoryOutlineChoiceOrder(qIdx, q) {
  const key = `hist_outline_${qIdx}`;
  const orders = getHistoryOutlineChoiceOrders();
  const saved = orders[key];
  if (Array.isArray(saved) && saved.length === q.opts.length && saved.every(i => Number.isInteger(i) && i >= 0 && i < q.opts.length)) {
    return saved;
  }
  const order = q.opts.map((_, i) => i);
  for (let i = order.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }
  orders[key] = order;
  setHistoryOutlineChoiceOrders(orders);
  return order;
}

function calculateHistoryOutlineScore() {
  const answers = getHistoryOutlineAnswers();
  let answered = 0, correct = 0;
  HISTORY_OUTLINE_ITEMS.forEach((item, idx) => {
    const ans = answers[`hist_outline_${idx}`];
    if (ans && ans.locked) {
      answered++;
      if (ans.correct) correct++;
    }
  });
  return { total: HISTORY_OUTLINE_ITEMS.length, answered, correct, wrong: answered - correct };
}

function resetHistoryOutlineQuiz() {
  if (!confirm('Reset only the History Outline Quiz progress? Bio and other History sections stay saved.')) return;
  setHistoryOutlineAnswers({});
  setHistoryOutlineChoiceOrders({});
  renderHistoryOutlineQuiz(document.getElementById('main-view'));
}

function renderHistoryOutlineQuiz(container) {
  const score = calculateHistoryOutlineScore();
  const pct = score.total ? Math.round((score.correct / score.total) * 100) : 0;
  const answeredPct = score.total ? Math.round((score.answered / score.total) * 100) : 0;
  const groups = [];
  HISTORY_OUTLINE_ITEMS.forEach((item, idx) => {
    const q = makeHistoryOutlineQuestion(item, idx);
    let group = groups.find(g => g.unit === q.unit);
    if (!group) {
      group = { unit: q.unit, items: [] };
      groups.push(group);
    }
    group.items.push({ q, idx });
  });

  container.innerHTML = `
    <div class="hero-panel" style="margin-bottom: 24px;">
      <div class="hero-eyebrow" style="color:var(--accent);">Teacher Outline Mode</div>
      <h1 style="font-family:'DM Serif Display', serif; font-size: clamp(24px, 3vw, 34px); line-height: 1.2; margin-bottom: 8px;">History Outline Quiz</h1>
      <p style="color: var(--text-secondary); font-size: 14.5px; max-width: 850px;">
        This follows the exact Unit 5-8 outline order. Every item is multiple choice only, no select-all, with shuffled answer choices saved per browser.
      </p>
      <div style="margin-top:16px; display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
        <div style="font-family:'DM Mono',monospace;font-size:13px;color:var(--text-secondary);"><strong>${score.correct}/${score.total}</strong> correct • <strong>${score.answered}</strong> answered • ${pct}% score</div>
        <div class="bar-container" style="width:min(360px,100%); margin:0;"><div class="bar-fill" style="width:${answeredPct}%"></div></div>
        <button class="q-btn" onclick="resetHistoryOutlineQuiz()" style="margin:0;border-color:var(--wrong);color:var(--wrong);font-weight:700;">Reset Outline Quiz</button>
      </div>
    </div>
    <div id="history-outline-list" style="display:flex; flex-direction:column; gap:20px;"></div>
  `;

  const list = document.getElementById('history-outline-list');
  groups.forEach(group => {
    const id = `hist-outline-${group.unit.replace(/[^a-zA-Z0-9]/g, '-')}`;
    const card = document.createElement('div');
    card.className = 'section-card';
    card.innerHTML = `
      <div class="section-header" onclick="toggleSectionBody('${id}')">
        <span class="section-title">${group.unit}</span>
        <span class="section-badge">${group.items.length} outline items</span>
        <span class="collapse-icon open">&#9660;</span>
      </div>
      <div class="section-body open" id="${id}"></div>
    `;
    list.appendChild(card);
    const body = card.querySelector('.section-body');
    group.items.forEach(({ q, idx }) => renderHistoryOutlineQuestion(body, q, idx));
  });
}

function renderHistoryOutlineQuestion(container, q, idx) {
  const key = `hist_outline_${idx}`;
  const answers = getHistoryOutlineAnswers();
  const saved = answers[key] || { selected: [], locked: false, correct: false };
  const order = getHistoryOutlineChoiceOrder(idx, q);
  const qBlock = document.createElement('div');
  qBlock.className = 'q-block';

  const meta = document.createElement('div');
  meta.className = 'q-meta';
  meta.innerHTML = `<span class="q-type-badge">Outline #${idx + 1}</span><span class="q-type-badge">${q.topic}</span>`;
  const stateBadge = document.createElement('span');
  stateBadge.className = 'q-state-badge';
  if (saved.locked) {
    stateBadge.classList.add(saved.correct ? 'correct' : 'wrong');
    stateBadge.textContent = saved.correct ? 'Correct' : 'Incorrect';
  }
  meta.appendChild(stateBadge);
  qBlock.appendChild(meta);

  const text = document.createElement('div');
  text.className = 'q-text';
  text.textContent = `${idx + 1}. ${q.q}`;
  qBlock.appendChild(text);

  const optsDiv = document.createElement('div');
  optsDiv.className = 'opts-container';
  order.forEach((optIdx, displayIdx) => {
    const label = document.createElement('label');
    label.className = 'opt-label';
    if (saved.selected.includes(optIdx)) label.classList.add('selected');
    if (saved.locked) {
      label.classList.add('locked');
      if (optIdx === q.a) label.classList.add('correct');
      else if (saved.selected.includes(optIdx)) label.classList.add('wrong');
    }
    const input = document.createElement('input');
    input.type = 'radio';
    input.className = 'opt-input';
    input.name = `hist_outline_${idx}`;
    input.value = optIdx;
    input.checked = saved.selected.includes(optIdx);
    input.disabled = saved.locked;
    input.addEventListener('change', () => {
      if (saved.locked) return;
      saved.selected = [optIdx];
      qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
      label.classList.add('selected');
      answers[key] = { selected: saved.selected, locked: false, correct: false };
      setHistoryOutlineAnswers(answers);
      const checkBtn = qBlock.querySelector('.check-answer-btn');
      if (checkBtn) checkBtn.style.display = 'inline-flex';
    });
    label.appendChild(input);
    const letter = document.createElement('span');
    letter.className = 'opt-letter';
    letter.textContent = String.fromCharCode(65 + displayIdx) + '.';
    label.appendChild(letter);
    const textSpan = document.createElement('span');
    textSpan.className = 'opt-text';
    textSpan.textContent = q.opts[optIdx];
    label.appendChild(textSpan);
    optsDiv.appendChild(label);
  });
  qBlock.appendChild(optsDiv);

  const feedback = document.createElement('div');
  feedback.className = 'q-feedback';
  if (saved.locked) {
    feedback.classList.add('show', saved.correct ? 'good' : 'bad');
    const correctDisplayIdx = order.indexOf(q.a);
    const userDisplayIdx = saved.selected.length ? order.indexOf(saved.selected[0]) : -1;
    feedback.innerHTML = saved.correct
      ? `<strong>Correct.</strong> ${q.explanation}`
      : `<strong>Incorrect.</strong> You chose ${userDisplayIdx >= 0 ? String.fromCharCode(65 + userDisplayIdx) : 'none'}; the correct answer is ${String.fromCharCode(65 + correctDisplayIdx)}.<br>${q.explanation}`;
  }
  qBlock.appendChild(feedback);

  const actions = document.createElement('div');
  actions.className = 'q-actions';
  if (!saved.locked) {
    const btn = document.createElement('button');
    btn.className = 'q-btn primary check-answer-btn';
    btn.textContent = 'Check Answer';
    btn.style.display = saved.selected.length ? 'inline-flex' : 'none';
    btn.addEventListener('click', () => {
      if (!saved.selected.length) return;
      answers[key] = { selected: saved.selected, locked: true, correct: saved.selected[0] === q.a };
      setHistoryOutlineAnswers(answers);
      renderHistoryOutlineQuiz(document.getElementById('main-view'));
    });
    actions.appendChild(btn);
  }
  qBlock.appendChild(actions);
  container.appendChild(qBlock);
}
