"""
patch_v2.py — Apply all requested changes:
1. Section stays open on reset/shuffle/original-order (don't re-render whole unit)
2. MP3 audio player instead of YouTube popup
3. Check Answer button for ALL question types (select first, then check)
4. Exam grading mode toggle (check at end recommended vs during test)
"""
import re

base_path = r"c:\Users\elieu\OneDrive\Desktop\biofinaltest\assemble_quiz.py"

with open(base_path, "r", encoding="utf-8") as f:
    content = f.read()

# ============================================================
# FIX 1: Section stays open on reset/shuffle/original-order
# Replace the three functions to only re-render the section questions, not the whole unit
# ============================================================
old_reset = """function resetSection(unitNum, sec) {
  if (!confirm('Reset all answers in section ' + sec + '? This will clear your progress for this section.')) return;
  
  const questions = QUIZ_DATA[unitNum] || [];
  let cleared = 0;
  questions.forEach((q, idx) => {
    if (q.section === sec) {
      const qKey = `q_${unitNum}_${sec}_${idx}`;
      if (appState.userAnswers[qKey]) {
        delete appState.userAnswers[qKey];
        cleared++;
      }
    }
  });
  
  saveState();
  updateDashboardUI();
  
  // Re-render this unit view to reflect cleared state
  const mainView = document.getElementById('main-view');
  renderUnitView(mainView, unitNum);
}

function shuffleSection(unitNum, sec) {
  const questions = QUIZ_DATA[unitNum] || [];
  // Get indices of questions in this section
  const sectionIndices = [];
  questions.forEach((q, idx) => {
    if (q.section === sec) sectionIndices.push(idx);
  });
  
  // Fisher-Yates shuffle on the indices
  const shuffled = [...sectionIndices];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  
  const key = `${unitNum}_${sec}`;
  sectionShuffleMap[key] = shuffled;
  saveShuffleState();
  
  // Re-render
  const mainView = document.getElementById('main-view');
  renderUnitView(mainView, unitNum);
}

function unshuffleSection(unitNum, sec) {
  const key = `${unitNum}_${sec}`;
  delete sectionShuffleMap[key];
  saveShuffleState();
  
  // Re-render
  const mainView = document.getElementById('main-view');
  renderUnitView(mainView, unitNum);
}"""

new_reset = """function reRenderSectionOnly(unitNum, sec) {
  const questions = QUIZ_DATA[unitNum] || [];
  const secQs = [];
  questions.forEach((q, idx) => {
    if (q.section === sec) secQs.push({ q, idx });
  });
  
  // Apply shuffle if exists
  const shuffleKey = `${unitNum}_${sec}`;
  let orderedQs = secQs;
  if (sectionShuffleMap[shuffleKey]) {
    const order = sectionShuffleMap[shuffleKey];
    const idxToEntry = {};
    secQs.forEach(entry => { idxToEntry[entry.idx] = entry; });
    const reordered = order.map(origIdx => idxToEntry[origIdx]).filter(Boolean);
    if (reordered.length === secQs.length) orderedQs = reordered;
  }
  
  const containerEl = document.getElementById(`sec-qs-container-${sec.replace('.', '_')}`);
  if (containerEl) renderSectionQuestions(containerEl, unitNum, sec, orderedQs);
  
  // Update section progress text
  let answered = 0;
  secQs.forEach(({ q, idx }) => {
    const qKey = `q_${unitNum}_${sec}_${idx}`;
    if (appState.userAnswers[qKey] && appState.userAnswers[qKey].locked) answered++;
  });
  const progEl = document.getElementById(`sec-prog-${sec.replace('.', '_')}`);
  if (progEl) progEl.textContent = `${answered} / ${secQs.length} completed`;
}

function resetSection(unitNum, sec) {
  if (!confirm('Reset all answers in section ' + sec + '? This will clear your progress for this section.')) return;
  
  const questions = QUIZ_DATA[unitNum] || [];
  questions.forEach((q, idx) => {
    if (q.section === sec) {
      const qKey = `q_${unitNum}_${sec}_${idx}`;
      delete appState.userAnswers[qKey];
    }
  });
  
  saveState();
  updateDashboardUI();
  reRenderSectionOnly(unitNum, sec);
}

function shuffleSection(unitNum, sec) {
  const questions = QUIZ_DATA[unitNum] || [];
  const sectionIndices = [];
  questions.forEach((q, idx) => {
    if (q.section === sec) sectionIndices.push(idx);
  });
  
  const shuffled = [...sectionIndices];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  
  const key = `${unitNum}_${sec}`;
  sectionShuffleMap[key] = shuffled;
  saveShuffleState();
  reRenderSectionOnly(unitNum, sec);
}

function unshuffleSection(unitNum, sec) {
  const key = `${unitNum}_${sec}`;
  delete sectionShuffleMap[key];
  saveShuffleState();
  reRenderSectionOnly(unitNum, sec);
}"""

if old_reset in content:
    content = content.replace(old_reset, new_reset)
    print("FIX 1: Section stays open on reset/shuffle/original-order - DONE")
else:
    print("FIX 1: WARNING - Could not find reset/shuffle block")

# ============================================================
# FIX 2: MP3 audio player instead of YouTube popup
# ============================================================
old_music_js = """// ── PHONK STATION YT PLAYER (POPUP WINDOW) ──
let phonkWindow = null;
let phonkPlaying = false;
let phonkCheckInterval = null;

function playMusic() {
  // Close existing popup if any
  if (phonkWindow && !phonkWindow.closed) {
    phonkWindow.close();
  }
  
  // Open YouTube in a small popup window — always works, no embed restrictions
  phonkWindow = window.open(
    'https://www.youtube.com/watch?v=wm9yxQiCuQ0&list=RDwm9yxQiCuQ0&start_radio=1&autoplay=1',
    'phonk_player',
    'width=420,height=320,left=100,top=100,menubar=no,toolbar=no,location=no,status=no,resizable=yes'
  );
  
  phonkPlaying = true;
  updateMusicUI('Playing');
  
  // Monitor if user closes the popup
  if (phonkCheckInterval) clearInterval(phonkCheckInterval);
  phonkCheckInterval = setInterval(() => {
    if (phonkWindow && phonkWindow.closed) {
      clearInterval(phonkCheckInterval);
      phonkPlaying = false;
      updateMusicUI('Stopped');
    }
  }, 1000);
}

function stopMusic() {
  if (phonkCheckInterval) clearInterval(phonkCheckInterval);
  if (phonkWindow && !phonkWindow.closed) {
    phonkWindow.close();
  }
  phonkWindow = null;
  phonkPlaying = false;
  updateMusicUI('Stopped');
}"""

new_music_js = """// ── PHONK STATION MP3 PLAYER ──
let phonkAudio = null;
let phonkPlaying = false;

function playMusic() {
  if (!phonkAudio) {
    phonkAudio = new Audio('YARA YARA PHONK (TOM SUIT PHONK) SLOWED TO PERFECTION. BEST PART.mp3');
    phonkAudio.loop = true;
    phonkAudio.addEventListener('error', () => {
      updateMusicUI('Stopped');
      alert('Could not load audio file. Make sure the MP3 is in the same folder as index.html.');
    });
  }
  
  phonkAudio.play().then(() => {
    phonkPlaying = true;
    updateMusicUI('Playing');
  }).catch(e => {
    console.error('Audio play failed:', e);
    updateMusicUI('Stopped');
  });
}

function stopMusic() {
  if (phonkAudio) {
    phonkAudio.pause();
    phonkAudio.currentTime = 0;
  }
  phonkPlaying = false;
  updateMusicUI('Stopped');
}"""

if old_music_js in content:
    content = content.replace(old_music_js, new_music_js)
    print("FIX 2: MP3 audio player - DONE")
else:
    print("FIX 2: WARNING - Could not find music JS block")

# ============================================================
# FIX 3: Check Answer button for ALL question types
# Replace the MC auto-grade behavior: select first, then click "Check Answer"
# ============================================================

# Change the MC immediate-grade behavior to just save selection, not grade
old_mc_handler = """          if (q.t === 'mc') {
          savedState.selected = [optIdx];
          // Highlight active label
          qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
          label.classList.add('selected');
          
          if (appState.feedbackMode === 'immediate') {
            gradeQuestion(unitNum, sec, idx, qBlock, q, savedState);
          } else {
            // Save state immediately (but unlocked)
            appState.userAnswers[qKey] = { selected: savedState.selected, locked: false, correct: false };
            localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
          }"""

new_mc_handler = """          if (q.t === 'mc') {
          savedState.selected = [optIdx];
          // Highlight active label
          qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
          label.classList.add('selected');
          
          // Always just save selection — user clicks "Check Answer" to grade
          appState.userAnswers[qKey] = { selected: savedState.selected, locked: false, correct: false };
          localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
          
          // Show the check answer button if hidden
          const checkBtn = qBlock.querySelector('.check-answer-btn');
          if (checkBtn) checkBtn.style.display = 'inline-flex';"""

if old_mc_handler in content:
    content = content.replace(old_mc_handler, new_mc_handler)
    print("FIX 3a: MC auto-grade removed, save-only on select - DONE")
else:
    print("FIX 3a: WARNING - Could not find MC handler")

# Change the SA (select-all) handler similarly
old_sa_handler = """          if (appState.feedbackMode === 'immediate') {
            // Check box immediate requires clicking a "Check" button, render below
          } else {
            appState.userAnswers[qKey] = { selected: savedState.selected, locked: false, correct: false };
            localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
          }"""

new_sa_handler = """          // Always save selection
          appState.userAnswers[qKey] = { selected: savedState.selected, locked: false, correct: false };
          localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
          
          // Show the check answer button if hidden
          const checkBtnSA = qBlock.querySelector('.check-answer-btn');
          if (checkBtnSA) checkBtnSA.style.display = 'inline-flex';"""

if old_sa_handler in content:
    content = content.replace(old_sa_handler, new_sa_handler)
    print("FIX 3b: SA auto-grade removed - DONE")
else:
    print("FIX 3b: WARNING - Could not find SA handler")

# Replace the old check button logic (was only for SA immediate) with a universal Check Answer button
old_actions = """    const actions = document.createElement('div');
    actions.className = 'q-actions';
    
    // If select-all and immediate grading, we need a submit button for this question
    if (q.t === 'sa' && appState.feedbackMode === 'immediate' && !savedState.locked) {
      const checkBtn = document.createElement('button');
      checkBtn.className = 'q-btn primary';
      checkBtn.textContent = 'Check Answer';
      checkBtn.addEventListener('click', () => {
        if (savedState.selected.length === 0) return;
        gradeQuestion(unitNum, sec, idx, qBlock, q, savedState);
      });
      actions.appendChild(checkBtn);
    }
    
    qBlock.appendChild(actions);"""

new_actions = """    const actions = document.createElement('div');
    actions.className = 'q-actions';
    
    // Universal Check Answer button for all question types
    if (!savedState.locked) {
      const checkBtn = document.createElement('button');
      checkBtn.className = 'q-btn primary check-answer-btn';
      checkBtn.textContent = 'Check Answer';
      checkBtn.style.display = savedState.selected.length > 0 ? 'inline-flex' : 'none';
      checkBtn.addEventListener('click', () => {
        if (savedState.selected.length === 0) return;
        gradeQuestion(unitNum, sec, idx, qBlock, q, savedState);
        checkBtn.style.display = 'none';
      });
      actions.appendChild(checkBtn);
    }
    
    qBlock.appendChild(actions);"""

if old_actions in content:
    content = content.replace(old_actions, new_actions)
    print("FIX 3c: Universal Check Answer button for all questions - DONE")
else:
    print("FIX 3c: WARNING - Could not find actions block")

# ============================================================
# FIX 4: Exam grading mode toggle
# Add examGradingMode to appState and a toggle in the exam room
# ============================================================

# Add examGradingMode to appState
old_appstate = """  // Final Exam Simulator Session State
  examSession: null, // Active exam session details (MC answers, text responses, time left)
  examResult: null   // Completed, graded exam results for review
};"""

new_appstate = """  // Final Exam Simulator Session State
  examSession: null, // Active exam session details (MC answers, text responses, time left)
  examResult: null,   // Completed, graded exam results for review
  examGradingMode: 'end' // 'end' (check at end, recommended) or 'during' (check during test)
};"""

if old_appstate in content:
    content = content.replace(old_appstate, new_appstate)
    print("FIX 4a: examGradingMode added to appState - DONE")
else:
    print("FIX 4a: WARNING - Could not find appState block")

# Add grading mode toggle to exam start page (before the Begin button)
old_begin_btn = """      <button class="exam-btn" onclick="startFinalExamSimulation()" style="background: var(--wrong); border-color: var(--wrong); width: 100%; font-size: 16px; padding: 14px 0;">
        Begin 2-Hour Final Exam Simulation
      </button>"""

new_begin_btn = """      <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 16px 20px; margin-bottom: 20px;">
        <div style="font-weight: 600; font-size: 14px; margin-bottom: 8px;">Answer Checking Mode</div>
        <label style="display:flex; align-items:center; gap:8px; cursor:pointer; padding:8px 0; font-size:13.5px;">
          <input type="radio" name="exam_grade_mode" value="end" checked onchange="appState.examGradingMode='end'">
          <span><strong>Check at the end</strong> <span style="color:var(--correct);font-weight:600;">(Recommended)</span> — Submit all answers at the end for grading, just like a real exam.</span>
        </label>
        <label style="display:flex; align-items:center; gap:8px; cursor:pointer; padding:8px 0; font-size:13.5px;">
          <input type="radio" name="exam_grade_mode" value="during" onchange="appState.examGradingMode='during'">
          <span><strong>Check during test</strong> — See feedback after each question as you go.</span>
        </label>
      </div>
      
      <button class="exam-btn" onclick="startFinalExamSimulation()" style="background: var(--wrong); border-color: var(--wrong); width: 100%; font-size: 16px; padding: 14px 0;">
        Begin 2-Hour Final Exam Simulation
      </button>"""

if old_begin_btn in content:
    content = content.replace(old_begin_btn, new_begin_btn)
    print("FIX 4b: Exam grading mode toggle UI added - DONE")
else:
    print("FIX 4b: WARNING - Could not find begin button")

# Now modify renderExamMCList to support "during" grading mode
# Add a Check Answer button per question in exam MC when mode is 'during'
old_exam_mc_end = """    qBlock.appendChild(optsDiv);
    container.appendChild(qBlock);
  });
}

function renderExamWrittenList"""

new_exam_mc_end = """    qBlock.appendChild(optsDiv);
    
    // If grading mode is 'during', add a Check Answer button per exam question
    if (appState.examGradingMode === 'during') {
      const fb = document.createElement('div');
      fb.className = 'q-feedback';
      fb.id = `exam-fb-${namePrefix}-${idx}`;
      qBlock.appendChild(fb);
      
      const checkBtn = document.createElement('button');
      checkBtn.className = 'q-btn primary check-answer-btn';
      checkBtn.textContent = 'Check Answer';
      checkBtn.style.marginTop = '8px';
      checkBtn.addEventListener('click', () => {
        if (answerArray[idx] === null || answerArray[idx] === undefined) return;
        const isCorrect = (answerArray[idx] === q.a);
        const userLetter = String.fromCharCode(65 + answerArray[idx]);
        const correctLetter = String.fromCharCode(65 + q.a);
        
        fb.className = 'q-feedback show ' + (isCorrect ? 'good' : 'bad');
        if (isCorrect) {
          fb.innerHTML = '<strong>\\u2713 Correct! You chose ' + correctLetter + '.</strong>';
        } else {
          fb.innerHTML = '<strong>\\u2717 Incorrect. You chose ' + userLetter + '. The correct answer is ' + correctLetter + '.</strong>';
        }
        
        // Show explanations
        if (q.explanations) {
          const expBox = document.createElement('div');
          expBox.style.cssText = 'margin-top:8px;font-size:13px;line-height:1.5;';
          q.explanations.forEach((exp, eIdx) => {
            const letter = String.fromCharCode(65 + eIdx);
            const p = document.createElement('p');
            p.style.marginBottom = '4px';
            if (eIdx === q.a) {
              p.style.color = 'var(--correct)';
              p.innerHTML = '<strong>' + letter + ' (Correct):</strong> ' + exp;
            } else if (eIdx === answerArray[idx]) {
              p.style.color = 'var(--wrong)';
              p.innerHTML = '<strong>' + letter + ' (Your Choice):</strong> ' + exp;
            } else {
              p.innerHTML = '<strong>' + letter + ':</strong> ' + exp;
            }
            expBox.appendChild(p);
          });
          fb.appendChild(expBox);
        }
        
        // Color the options
        qBlock.querySelectorAll('.opt-label').forEach((lbl, oIdx) => {
          lbl.classList.add('locked');
          lbl.style.pointerEvents = 'none';
          if (oIdx === q.a) lbl.classList.add('correct');
          else if (oIdx === answerArray[idx]) lbl.classList.add('wrong');
        });
        
        checkBtn.style.display = 'none';
      });
      qBlock.appendChild(checkBtn);
    }
    
    container.appendChild(qBlock);
  });
}

function renderExamWrittenList"""

if old_exam_mc_end in content:
    content = content.replace(old_exam_mc_end, new_exam_mc_end)
    print("FIX 4c: Exam 'during' mode check answer per question - DONE")
else:
    print("FIX 4c: WARNING - Could not find exam MC end block")

# ============================================================
# SAVE
# ============================================================
with open(base_path, "w", encoding="utf-8") as f:
    f.write(content)

print("\nAll patches applied! Now regenerating index.html...")

import subprocess, os
result = subprocess.run(["python", os.path.join(r"c:\Users\elieu\OneDrive\Desktop\biofinaltest", "assemble_quiz.py")],
    cwd=r"c:\Users\elieu\OneDrive\Desktop\biofinaltest", capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
if result.returncode == 0:
    size = os.path.getsize(os.path.join(r"c:\Users\elieu\OneDrive\Desktop\biofinaltest", "index.html"))
    print(f"SUCCESS! index.html regenerated ({size:,} bytes)")
else:
    print(f"ERROR: Return code {result.returncode}")
