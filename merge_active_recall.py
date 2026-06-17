import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).parent
TARGET = ROOT / "index - Copy.html"


recall = {}
for unit in range(1, 9):
    recall[str(unit)] = json.loads(
        (ROOT / f"unit{unit}_active_recall.json").read_text(encoding="utf-8-sig")
    )

payload = "const ACTIVE_RECALL_DATA = " + json.dumps(
    recall, ensure_ascii=False, separators=(",", ":")
) + ";"

css = r"""
  body.recall-active .layout-container { max-width:min(1760px,calc(100vw - 28px)); grid-template-columns:minmax(0,1fr); padding-left:14px; padding-right:14px; }
  body.recall-active .sidebar { display:none; }
  body.recall-active .main-content { width:100%; min-width:0; }
  .recall-shell { width:100%; }
  .recall-hero { max-width:var(--recall-reading-width,1080px); margin-left:auto; margin-right:auto; }
  .recall-toolbar { display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; margin-top:18px; padding-top:16px; border-top:1px solid var(--border); }
  .recall-width-control { display:flex; align-items:center; flex-wrap:wrap; gap:8px; }
  .recall-width-control label { font-size:12px; font-weight:700; color:var(--text-secondary); }
  .recall-width-control input[type="range"] { width:min(280px,42vw); accent-color:var(--accent); }
  .recall-width-value { min-width:58px; font:500 11px 'DM Mono',monospace; color:var(--text-dim); }
  .recall-layout { display:grid; grid-template-columns:minmax(0,1fr); gap:16px; align-items:start; overflow-anchor:none; }
  .recall-unit-list { position:sticky; top:74px; z-index:15; display:flex; align-items:center; gap:7px; max-width:var(--recall-reading-width,1080px); margin:0 auto; padding:10px; overflow-x:auto; }
  .recall-unit-list .dashboard-title { flex:0 0 auto; margin:0 4px 0 2px; }
  .recall-unit-list .unit-nav-btn { flex:0 0 auto; width:auto; min-width:112px; margin:0; }
  #recall-page-host { position:relative; width:min(100%,var(--recall-reading-width,1080px)); margin:0 auto; }
  .recall-page-card { width:100%; background:var(--surface); border:1px solid var(--border); border-radius:12px; overflow:visible; }
  .recall-resize-handle { position:absolute; top:80px; right:-13px; bottom:95px; width:18px; cursor:ew-resize; z-index:14; touch-action:none; }
  .recall-resize-handle::after { content:''; position:absolute; left:8px; top:0; bottom:0; width:3px; border-radius:4px; background:var(--accent); opacity:.28; transition:opacity .15s,box-shadow .15s; }
  .recall-resize-handle:hover::after,.recall-resize-handle.dragging::after { opacity:.8; box-shadow:0 0 0 4px var(--accent-soft); }
  .recall-reading { padding:clamp(20px,3vw,34px); font-size:16px; line-height:1.72; }
  .recall-reading h2 { font-family:'DM Serif Display',serif; font-size:clamp(24px,3vw,30px); line-height:1.2; margin:8px 0 18px; }
  .recall-explanation { margin-bottom:22px; }
  .recall-page-actions { display:flex; flex-wrap:wrap; gap:9px; margin:18px 0; }
  .recall-source { margin:22px 0; border:1px solid var(--border); border-radius:9px; background:var(--surface2); }
  .recall-source summary { cursor:pointer; padding:13px 15px; font-weight:700; }
  .recall-source-text { padding:0 15px 16px; white-space:pre-wrap; line-height:1.62; color:var(--text-secondary); }
  .recall-question { margin-top:20px; padding:clamp(15px,2.5vw,21px); background:var(--surface2); border:1px solid var(--border); border-radius:9px; }
  .recall-option { display:flex; align-items:flex-start; gap:10px; padding:11px 12px; border:1px solid var(--border); border-radius:7px; margin-top:8px; cursor:pointer; line-height:1.45; }
  .recall-option input { margin-top:4px; flex:0 0 auto; }
  .recall-option.correct { border-color:var(--correct); background:var(--correct-soft); }
  .recall-option.wrong { border-color:var(--wrong); background:var(--wrong-soft); }
  .recall-written-answer { width:100%; min-height:110px; resize:vertical; margin-top:12px; padding:12px; border:1px solid var(--border-strong); border-radius:7px; background:var(--surface); color:var(--text-primary); font:inherit; line-height:1.5; }
  .recall-page-nav { position:sticky; bottom:12px; z-index:12; display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:10px; margin:0 14px 14px; padding:12px; border:1px solid var(--border-strong); border-radius:11px; background:color-mix(in srgb,var(--surface) 94%,transparent); box-shadow:0 8px 30px rgba(0,0,0,.18); backdrop-filter:blur(12px); }
  .recall-page-status { min-width:118px; text-align:center; font-weight:700; white-space:nowrap; }
  .recall-page-jump { display:flex; align-items:center; gap:7px; white-space:nowrap; }
  .recall-page-jump input { width:76px; padding:8px 9px; border:1px solid var(--border-strong); border-radius:6px; background:var(--surface); color:var(--text-primary); text-align:center; font:inherit; }
  .recall-page-nav .q-btn { margin:0; }
  body.notes-open.recall-active .layout-container { max-width:none; margin-left:0; }
  body.notes-open .recall-unit-list { position:static; max-width:100%; }
  body.notes-open #recall-page-host { width:100%; }
  body.notes-open .recall-resize-handle { display:none; }
  body.notes-open .recall-reading { padding:18px; }
  body.notes-open .recall-page-nav { margin:0 7px 7px; padding:8px; gap:6px; }
  body.notes-open .recall-page-nav .q-btn { padding:8px 9px; }
  body.notes-open .recall-page-status { width:100%; min-width:0; }
  @media(max-width:800px){
    body.recall-active .layout-container{max-width:none;padding:10px}
    .recall-hero{max-width:none}
    .recall-layout{gap:12px}
    .recall-unit-list{position:static;max-width:none}
    .recall-resize-handle{display:none}
    .recall-reading{padding:19px}
    .recall-page-nav{bottom:7px;margin:0 7px 7px;padding:9px;gap:7px}
    .recall-page-nav .q-btn{padding:9px 11px}
    .recall-page-status{order:-1;width:100%}
  }
"""

functions = r"""
let recallState = {
  answers: (() => { try { return JSON.parse(localStorage.getItem('quiz_recall_answers_v1') || '{}'); } catch(e) { return {}; } })(),
  unit: Number(localStorage.getItem('quiz_recall_unit_v1') || 1),
  page: Number(localStorage.getItem('quiz_recall_page_v1') || 0),
  width: Math.max(680, Math.min(1400, Number(localStorage.getItem('quiz_recall_width_v1') || 1080)))
};

function saveRecallState() {
  localStorage.setItem('quiz_recall_answers_v1', JSON.stringify(recallState.answers));
  localStorage.setItem('quiz_recall_unit_v1', String(recallState.unit));
  localStorage.setItem('quiz_recall_page_v1', String(recallState.page));
  localStorage.setItem('quiz_recall_width_v1', String(recallState.width));
}

function recallAnswerKey(pageData, questionIndex) {
  return `${pageData.filename}_${pageData.page_num_in_file}_${questionIndex}`;
}

function legacyRecallAnswer(pageData, questionIndex) {
  if (!Number.isInteger(pageData.legacy_index)) return null;
  return recallState.answers[`${recallState.unit}_${pageData.legacy_index}_${questionIndex}`] || null;
}

function savedRecallAnswer(pageData, questionIndex) {
  return recallState.answers[recallAnswerKey(pageData, questionIndex)] || legacyRecallAnswer(pageData, questionIndex);
}

function recallUnitStats(unit) {
  const pages = ACTIVE_RECALL_DATA[unit] || [];
  let completed = 0;
  pages.forEach(pageData => {
    if (!pageData.questions.length || pageData.questions.every((q, qi) => savedRecallAnswer(pageData, qi)?.locked)) completed++;
  });
  return { completed, total: pages.length };
}

function renderActiveRecall(container) {
  applyRecallReadingWidth();
  const units = Object.keys(ACTIVE_RECALL_DATA).map(Number);
  if (!units.includes(recallState.unit)) recallState.unit = 1;
  const pages = ACTIVE_RECALL_DATA[recallState.unit] || [];
  recallState.page = Math.max(0, Math.min(recallState.page, Math.max(0, pages.length - 1)));
  container.innerHTML = `<div class="recall-shell">
    <div class="hero-panel recall-hero">
      <div class="hero-eyebrow">Biology · Reading Active Recall</div>
      <h1>Read Every Page. Recall Every Idea.</h1>
      <p>All 1,025 PDF pages are included in their original order. Progress is saved separately from the existing study guide.</p>
      <div class="recall-toolbar">
        <button class="q-btn" onclick="showView('dashboard')">Back to Study Dashboard</button>
        <div class="recall-width-control">
          <label for="recall-width-slider">Reading width</label>
          <button class="q-btn" onclick="setRecallReadingWidth(820)">Narrow</button>
          <button class="q-btn" onclick="setRecallReadingWidth(1080)">Default</button>
          <button class="q-btn" onclick="setRecallReadingWidth(1320)">Wide</button>
          <input id="recall-width-slider" type="range" min="680" max="1400" step="20" value="${recallState.width}" oninput="setRecallReadingWidth(this.value)">
          <span class="recall-width-value" id="recall-width-value">${recallState.width}px</span>
        </div>
      </div>
    </div>
    <div class="recall-layout">
      <div class="sidebar-box recall-unit-list">
        <h2 class="dashboard-title">Units</h2>
        ${units.map(unit => {
          const stats = recallUnitStats(unit);
          const pct = stats.total ? Math.round(stats.completed / stats.total * 100) : 0;
          return `<button class="unit-nav-btn ${unit===recallState.unit?'active':''}" onclick="selectRecallUnit(${unit})"><span class="unit-nav-name">Unit ${unit}</span><span class="unit-nav-progress">${stats.total} pages · ${pct}%</span></button>`;
        }).join('')}
      </div>
      <div id="recall-page-host"></div>
    </div></div>`;
  renderRecallPage();
}

function applyRecallReadingWidth() {
  document.documentElement.style.setProperty('--recall-reading-width', `${recallState.width}px`);
}

function setRecallReadingWidth(width) {
  recallState.width = Math.max(680, Math.min(1400, Number(width) || 1080));
  applyRecallReadingWidth();
  localStorage.setItem('quiz_recall_width_v1', String(recallState.width));
  const slider = document.getElementById('recall-width-slider');
  const value = document.getElementById('recall-width-value');
  if (slider) slider.value = recallState.width;
  if (value) value.textContent = `${recallState.width}px`;
}

function startRecallResize(event) {
  if (document.body.classList.contains('notes-open') || window.innerWidth <= 800) return;
  event.preventDefault();
  const handle = event.currentTarget;
  handle.classList.add('dragging');
  handle.setPointerCapture?.(event.pointerId);
  const move = moveEvent => {
    const centeredWidth = Math.round(Math.abs(moveEvent.clientX - window.innerWidth / 2) * 2 / 20) * 20;
    setRecallReadingWidth(centeredWidth);
  };
  const stop = () => {
    handle.classList.remove('dragging');
    window.removeEventListener('pointermove', move);
    window.removeEventListener('pointerup', stop);
    window.removeEventListener('pointercancel', stop);
  };
  window.addEventListener('pointermove', move);
  window.addEventListener('pointerup', stop, { once:true });
  window.addEventListener('pointercancel', stop, { once:true });
}

function selectRecallUnit(unit) {
  recallState.unit = unit;
  recallState.page = 0;
  saveRecallState();
  renderActiveRecall(document.getElementById('main-view'));
}

function renderRecallPage(options = {}) {
  const previousScrollY = options.preserveScroll ? window.scrollY : 0;
  const host = document.getElementById('recall-page-host');
  const pages = ACTIVE_RECALL_DATA[recallState.unit] || [];
  const pageData = pages[recallState.page];
  if (!pageData) {
    host.innerHTML = '<div class="sidebar-box">No recall pages found for this unit.</div>';
    return;
  }
  const lessonInfo = recallLessonInfo(pageData);
  const lessonProgress = recallLessonProgress(pages, pageData);
  host.innerHTML = `<div class="recall-resize-handle" onpointerdown="startRecallResize(event)" title="Drag to resize the reading area" aria-label="Resize reading area"></div><div class="recall-page-card">
    <div class="recall-reading">
      <div class="hero-eyebrow">Unit ${lessonInfo.unit} · Lesson ${lessonInfo.lesson} · Lesson Page ${lessonProgress.current} of ${lessonProgress.total} · Unit Page ${recallState.page + 1} of ${pages.length} · ${escapeRecall(pageData.section_title || '')}</div>
      <h2>${escapeRecall(pageData.slide_title || pageData.section_title || 'Biology Notes')}</h2>
      <div class="recall-explanation">${escapeRecall(pageData.explanation || '').replace(/\n/g, '<br><br>')}</div>
      <div class="recall-page-actions">
        <button class="q-btn" onclick="openRecallNotesPage(ACTIVE_RECALL_DATA[recallState.unit][recallState.page])">Open Exact Notes Page</button>
      </div>
      <details class="recall-source">
        <summary>Complete text from this notes page</summary>
        <div class="recall-source-text">${escapeRecall(pageData.original_text || '')}</div>
      </details>
      <div id="recall-questions">${renderRecallQuestions(pageData)}</div>
    </div>
    <div class="recall-page-nav" aria-label="Active recall page navigation">
      <button class="q-btn" onclick="moveRecallPage(-1)" ${recallState.page===0?'disabled':''}>Previous</button>
      <div class="recall-page-status">Page ${recallState.page + 1} of ${pages.length}</div>
      <form class="recall-page-jump" onsubmit="jumpToRecallPage(event)">
        <label for="recall-page-input">Go to</label>
        <input id="recall-page-input" type="number" inputmode="numeric" min="1" max="${pages.length}" value="${recallState.page + 1}" aria-label="Go to page number">
        <button class="q-btn" type="submit">Go</button>
      </form>
      <button class="q-btn primary" onclick="moveRecallPage(1)" ${recallState.page===pages.length-1?'disabled':''}>Next</button>
      <button class="q-btn danger" onclick="resetRecallUnit(${recallState.unit})">Reset Unit</button>
    </div>
  </div>`;
  saveRecallState();
  window.scrollTo({ top: previousScrollY, behavior: 'instant' });
  if (options.preserveScroll) {
    requestAnimationFrame(() => requestAnimationFrame(() => window.scrollTo({ top: previousScrollY, behavior: 'instant' })));
  }
}

function escapeRecall(value) {
  const div = document.createElement('div');
  div.textContent = String(value);
  return div.innerHTML;
}

function openRecallNotesPage(pageData) {
  const lessonInfo = recallLessonInfo(pageData);
  openSectionNotes(`${lessonInfo.unit}.${lessonInfo.lesson}`, Number(pageData.page_num_in_file) || 1);
}

function recallLessonInfo(pageData) {
  const match = String(pageData.filename || '').match(/^Unit_(\d+)_(\d+)\.txt$/);
  return {
    unit: match ? Number(match[1]) : recallState.unit,
    lesson: match ? Number(match[2]) : 1
  };
}

function recallLessonProgress(pages, pageData) {
  const lessonPages = pages.filter(page => page.filename === pageData.filename);
  return {
    current: Math.max(1, lessonPages.findIndex(page => page.page_num_in_file === pageData.page_num_in_file) + 1),
    total: lessonPages.length
  };
}

function renderRecallQuestions(pageData) {
  if (!pageData.questions || !pageData.questions.length) return '<p class="muted">Read this page, then continue.</p>';
  return pageData.questions.map((q, qi) => {
    const saved = savedRecallAnswer(pageData, qi);
    if (q.type === 'recall' || !Array.isArray(q.opts)) {
      return `<div class="recall-question" id="recall-q-${qi}">
        <strong>${qi + 1}. ${escapeRecall(q.q)}</strong>
        <textarea class="recall-written-answer" id="recall-written-${qi}" placeholder="Type everything you remember before revealing the answer.">${escapeRecall(saved?.written || '')}</textarea>
        ${saved?.locked ? `<div class="q-feedback show good">${escapeRecall(q.answer || q.exp || '')}</div>` :
        `<button class="q-btn primary" style="margin-top:10px;" onclick="revealRecallAnswer(${qi})">Reveal Answer</button>`}
      </div>`;
    }
    return `<div class="recall-question" id="recall-q-${qi}">
      <strong>${qi + 1}. ${escapeRecall(q.q)}</strong>
      <div>${q.opts.map((opt, oi) => `<label class="recall-option ${saved?.locked ? (oi===q.a?'correct':saved.selected===oi?'wrong':'') : ''}">
        <input type="radio" name="recall-${qi}" value="${oi}" ${saved?.selected===oi?'checked':''} ${saved?.locked?'disabled':''}>
        <span>${String.fromCharCode(65+oi)}. ${escapeRecall(opt)}</span>
      </label>`).join('')}</div>
      ${saved?.locked ? `<div class="q-feedback show ${saved.correct?'good':'bad'}">${saved.correct?'Correct.':'Incorrect.'} ${escapeRecall(q.exp || '')}</div>` :
      `<button class="q-btn primary" style="margin-top:10px;" onclick="gradeRecallQuestion(${qi})">Check Answer</button>`}
    </div>`;
  }).join('');
}

function gradeRecallQuestion(questionIndex) {
  const pageData = ACTIVE_RECALL_DATA[recallState.unit][recallState.page];
  const chosen = document.querySelector(`input[name="recall-${questionIndex}"]:checked`);
  if (!chosen) { alert('Choose an answer first.'); return; }
  const selected = Number(chosen.value);
  const question = pageData.questions[questionIndex];
  recallState.answers[recallAnswerKey(pageData, questionIndex)] = {
    selected, locked:true, correct:selected===question.a
  };
  saveRecallState();
  renderRecallPage({ preserveScroll: true });
}

function revealRecallAnswer(questionIndex) {
  const pageData = ACTIVE_RECALL_DATA[recallState.unit][recallState.page];
  const input = document.getElementById(`recall-written-${questionIndex}`);
  recallState.answers[recallAnswerKey(pageData, questionIndex)] = {
    written: input ? input.value : '', locked:true, correct:true
  };
  saveRecallState();
  renderRecallPage({ preserveScroll: true });
}

function moveRecallPage(direction) {
  const pages = ACTIVE_RECALL_DATA[recallState.unit] || [];
  recallState.page = Math.max(0, Math.min(pages.length - 1, recallState.page + direction));
  saveRecallState();
  renderRecallPage();
}

function jumpToRecallPage(event) {
  event.preventDefault();
  const pages = ACTIVE_RECALL_DATA[recallState.unit] || [];
  const input = document.getElementById('recall-page-input');
  const requested = Number.parseInt(input.value, 10);
  if (!Number.isFinite(requested) || requested < 1 || requested > pages.length) {
    input.value = recallState.page + 1;
    input.focus();
    return;
  }
  recallState.page = requested - 1;
  saveRecallState();
  renderRecallPage();
}

function resetRecallUnit(unit) {
  if (!confirm(`Reset Reading Active Recall answers for Unit ${unit}? Existing quiz progress will not be changed.`)) return;
  const prefixes = (ACTIVE_RECALL_DATA[unit] || []).map(page => `${page.filename}_${page.page_num_in_file}_`);
  Object.keys(recallState.answers).forEach(key => {
    if (key.startsWith(`${unit}_`) || prefixes.some(prefix => key.startsWith(prefix))) delete recallState.answers[key];
  });
  saveRecallState();
  renderActiveRecall(document.getElementById('main-view'));
}

"""


html = TARGET.read_text(encoding="utf-8")
html, data_replacements = re.subn(
    r"const ACTIVE_RECALL_DATA = .*?;\s*\n\s*const HISTORY_QUIZ_DATA =",
    lambda _: payload + "\n\nconst HISTORY_QUIZ_DATA =",
    html,
    count=1,
    flags=re.S,
)
if data_replacements != 1:
    raise RuntimeError("Could not replace ACTIVE_RECALL_DATA")

html, css_replacements = re.subn(
    r"\n\s*(?:body\.recall-active \.layout-container|\.recall-layout) \{.*?(?=\n</style>)",
    "\n" + css + "\n",
    html,
    count=1,
    flags=re.S,
)
if css_replacements != 1:
    raise RuntimeError("Could not replace active recall CSS")

html, function_replacements = re.subn(
    r"let recallState = \{.*?(?=function renderHistoryDashboard\(container\) \{)",
    lambda _: functions + "\n",
    html,
    count=1,
    flags=re.S,
)
if function_replacements != 1:
    raise RuntimeError("Could not replace active recall functions")

if "classList.toggle('recall-active'" not in html:
    html = html.replace(
        "  appState.currentView = viewId;\n",
        "  appState.currentView = viewId;\n"
        "  document.body.classList.toggle('recall-active', viewId === 'active-recall' && appState.subject === 'bio');\n",
        1,
    )

html = html.replace(
    '<span class="unit-nav-progress">1,000 pages</span>',
    '<span class="unit-nav-progress">1,025 pages</span>',
)
TARGET.write_text(html, encoding="utf-8", newline="")
shutil.copyfile(TARGET, ROOT / "index.html")
print(f"Merged {sum(len(v) for v in recall.values())} active recall pages into both HTML files.")
