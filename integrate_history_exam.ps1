$ErrorActionPreference = 'Stop'
$path = Join-Path $PSScriptRoot 'index.html'
$html = [IO.File]::ReadAllText($path)
$objective = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'history_exam_objective.json')).Trim()
$documents = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'history_exam_documents.json')).Trim()
$open = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'history_exam_open.json')).Trim()
$data = "const HISTORY_EXAM_DATA = {objective:$objective,documents:$documents,open:$open};`r`n"
$html = $html.Replace('let ACTIVE_QUIZ_DATA = QUIZ_DATA;', "let ACTIVE_QUIZ_DATA = QUIZ_DATA;`r`n$data")
$html = $html.Replace(
  "  } else if (viewId === 'final-exam-simulator') {`r`n    renderFinalExamView(mainView);",
  "  } else if (viewId === 'final-exam-simulator') {`r`n    renderFinalExamView(mainView);`r`n  } else if (viewId === 'history-final-exam') {`r`n    renderHistoryFinalExam(mainView);"
)
$anchor = '// Shuffles an array helper'
$code = @'
function historyExamStorageKey(kind) { return `history_final_exam_${kind}_v1`; }
function loadHistoryExam(kind) {
  try { return JSON.parse(localStorage.getItem(historyExamStorageKey(kind)) || 'null'); } catch(e) { return null; }
}
function saveHistoryExam(kind, value) {
  if (value) localStorage.setItem(historyExamStorageKey(kind), JSON.stringify(value));
  else localStorage.removeItem(historyExamStorageKey(kind));
}
function renderHistoryFinalExam(container) {
  const result = loadHistoryExam('result');
  const session = loadHistoryExam('session');
  if (result) return renderHistoryExamReview(container, result);
  if (session) return renderHistoryExamRoom(container, session);
  container.innerHTML = `<div class="exam-lobby-card">
    <div class="hero-eyebrow" style="color:var(--accent);">World History Final Exam Simulation</div>
    <h1 style="font-family:'DM Serif Display',serif;font-size:32px;margin-bottom:12px;">2025-26 World History Practice Final</h1>
    <p style="color:var(--text-secondary);margin-bottom:18px;">This simulator follows the exact structure supplied by your teacher and is graded out of 150 points.</p>
    <div class="exam-parts-grid">
      <div class="exam-part-card"><div class="exam-part-num">Section 1</div><strong>90 Objective Questions</strong><p>90 points</p></div>
      <div class="exam-part-card"><div class="exam-part-num">Section 2</div><strong>30 Document-based Objective Questions</strong><p>30 points</p></div>
      <div class="exam-part-card"><div class="exam-part-num">Section 3</div><strong>2 Open-ended Responses</strong><p>15 points each</p></div>
    </div>
    <div style="margin:18px 0;padding:14px;background:var(--amber-soft);border:1px solid var(--amber-border);border-radius:8px;color:var(--amber-ink);">
      <strong>Real exam reminders:</strong> The test is on paper. Bring pens and pencils. A documents packet will be provided, and you may not bring your own packet. If more than half of the ninth grade misses a question, the teacher may invalidate it.
    </div>
    <button class="exam-btn" onclick="startHistoryFinalExam()" style="width:100%;font-size:16px;padding:14px 0;">Start Practice Final</button>
  </div>`;
}
function startHistoryFinalExam() {
  const session = {
    objective: Array(90).fill(null),
    documents: Array(30).fill(null),
    essays: ['', ''],
    essayScores: [0, 0],
    startedAt: Date.now()
  };
  saveHistoryExam('session', session);
  showView('history-final-exam');
}
function renderHistoryExamMC(container, questions, answers, prefix, withDocument) {
  container.innerHTML = '';
  questions.forEach((q, i) => {
    const block = document.createElement('div');
    block.className = 'question-block';
    block.innerHTML = `${withDocument ? `<div style="padding:12px;background:var(--surface2);border-left:4px solid var(--accent);margin-bottom:12px;"><strong>Document:</strong> ${q.document}</div>` : ''}
      <div class="q-header"><span class="q-num">${i + 1}</span><div class="q-text">${q.q}</div></div>
      <div class="options-list">${q.opts.map((o,j)=>`<label class="opt-label"><input type="radio" name="${prefix}_${i}" value="${j}" ${answers[i]===j?'checked':''}><span class="opt-letter">${String.fromCharCode(65+j)}</span><span>${o}</span></label>`).join('')}</div>`;
    block.querySelectorAll('input').forEach(input => input.onchange = () => {
      const session = loadHistoryExam('session');
      session[prefix][i] = Number(input.value);
      saveHistoryExam('session', session);
    });
    container.appendChild(block);
  });
}
function renderHistoryExamRoom(container, session) {
  container.innerHTML = `<div class="hero-panel"><div class="hero-eyebrow">Practice Final In Progress</div><h1>World History Final Exam</h1><p>120 objective points + 30 open-response points = 150 total. Your work autosaves in this browser.</p></div>
    <div class="section-card"><div class="section-header"><span class="section-title">Section 1 - 90 Objective Questions</span></div><div class="section-body open" id="history-exam-objective"></div></div>
    <div class="section-card"><div class="section-header"><span class="section-title">Section 2 - 30 Document-based Objective Questions</span></div><div class="section-body open" id="history-exam-documents"></div></div>
    <div class="section-card"><div class="section-header"><span class="section-title">Section 3 - 2 Open-ended Responses</span></div><div class="section-body open" id="history-exam-open"></div></div>
    <div style="display:flex;gap:12px;margin-top:20px;"><button class="q-btn" onclick="if(confirm('Delete this attempt?')){saveHistoryExam('session',null);showView('history-final-exam')}">Reset Attempt</button><button class="exam-btn" style="flex:1;" onclick="submitHistoryFinalExam()">Submit Final Exam</button></div>`;
  renderHistoryExamMC(document.getElementById('history-exam-objective'), HISTORY_EXAM_DATA.objective, session.objective, 'objective', false);
  renderHistoryExamMC(document.getElementById('history-exam-documents'), HISTORY_EXAM_DATA.documents, session.documents, 'documents', true);
  const openBox = document.getElementById('history-exam-open');
  openBox.innerHTML = HISTORY_EXAM_DATA.open.map((q,i)=>`<div class="question-block"><h3 style="font-family:'DM Serif Display',serif;font-size:20px;margin-bottom:8px;">${i+1}. ${q.title}</h3><p style="white-space:pre-line;margin-bottom:12px;">${q.prompt}</p><textarea id="history-essay-${i}" style="width:100%;min-height:240px;padding:12px;background:var(--surface);color:var(--text-primary);border:1px solid var(--border-strong);border-radius:7px;font:inherit;">${session.essays[i]||''}</textarea></div>`).join('');
  HISTORY_EXAM_DATA.open.forEach((q,i)=>document.getElementById(`history-essay-${i}`).oninput = e => { const s=loadHistoryExam('session'); s.essays[i]=e.target.value; saveHistoryExam('session',s); });
}
function submitHistoryFinalExam() {
  const session = loadHistoryExam('session');
  const unanswered = session.objective.filter(v=>v===null).length + session.documents.filter(v=>v===null).length;
  if (unanswered && !confirm(`You still have ${unanswered} unanswered objective questions. Submit anyway?`)) return;
  let objectiveScore=0, documentScore=0;
  HISTORY_EXAM_DATA.objective.forEach((q,i)=>{if(session.objective[i]===q.a)objectiveScore++;});
  HISTORY_EXAM_DATA.documents.forEach((q,i)=>{if(session.documents[i]===q.a)documentScore++;});
  saveHistoryExam('result',{...session,objectiveScore,documentScore,essayScores:[0,0],submittedAt:Date.now()});
  saveHistoryExam('session',null);
  showView('history-final-exam');
}
function setHistoryEssayScore(index, score) {
  const result=loadHistoryExam('result'); result.essayScores[index]=Number(score); saveHistoryExam('result',result); showView('history-final-exam');
}
function renderHistoryExamReview(container, result) {
  const essayTotal=result.essayScores.reduce((a,b)=>a+b,0), total=result.objectiveScore+result.documentScore+essayTotal;
  container.innerHTML=`<div class="hero-panel"><div class="hero-eyebrow">Graded Practice Final</div><h1>${total} / 150 Points</h1><p>Objective: ${result.objectiveScore}/90 · Documents: ${result.documentScore}/30 · Open responses: ${essayTotal}/30</p></div>
    <div class="section-card"><div class="section-header"><span class="section-title">Open-response self-grading</span></div><div class="section-body open">${HISTORY_EXAM_DATA.open.map((q,i)=>`<div class="question-block"><h3>${q.title}</h3><p style="white-space:pre-line"><strong>Your response:</strong><br>${result.essays[i]||'(blank)'}</p><details style="margin-top:12px"><summary>View 15-point rubric and model answer</summary><pre style="white-space:pre-wrap;font:inherit;margin-top:10px;">${JSON.stringify(q.rubric,null,2)}</pre><p style="white-space:pre-line;margin-top:10px;"><strong>Model answer:</strong><br>${q.modelAnswer}</p></details><label style="display:block;margin-top:12px;">Score this response (0-15): <input type="number" min="0" max="15" value="${result.essayScores[i]}" onchange="setHistoryEssayScore(${i},Math.max(0,Math.min(15,this.value)))" style="width:70px;padding:6px;"></label></div>`).join('')}</div></div>
    <div class="section-card"><div class="section-header"><span class="section-title">Objective answer review</span></div><div class="section-body open" id="history-exam-review"></div></div>
    <button class="q-btn danger" onclick="if(confirm('Start a new practice final?')){saveHistoryExam('result',null);startHistoryFinalExam()}">Start New Attempt</button>`;
  const review=document.getElementById('history-exam-review');
  [...HISTORY_EXAM_DATA.objective.map((q,i)=>[q,result.objective[i],`Section 1 #${i+1}`]),...HISTORY_EXAM_DATA.documents.map((q,i)=>[q,result.documents[i],`Section 2 #${i+1}`])].forEach(([q,a,label])=>{
    const div=document.createElement('div'); div.className='question-block'; const ok=a===q.a;
    div.innerHTML=`<div class="q-header"><span class="q-state-badge ${ok?'correct':'wrong'}">${ok?'Correct':'Incorrect'}</span><div class="q-text">${label}: ${q.q}</div></div><p><strong>Your answer:</strong> ${a===null?'Unanswered':String.fromCharCode(65+a)} · <strong>Correct:</strong> ${String.fromCharCode(65+q.a)}</p><div class="q-feedback show ${ok?'good':'bad'}">${q.explanations[q.a]}</div>`;
    review.appendChild(div);
  });
}

'@
$html = $html.Replace($anchor, $code + $anchor)
[IO.File]::WriteAllText($path,$html,(New-Object Text.UTF8Encoding($false)))
Write-Host 'History final exam integrated.'
