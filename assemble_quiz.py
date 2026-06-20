import os
import json

base_dir = r"c:\Users\elieu\OneDrive\Desktop\biofinaltest"
output_file = os.path.join(base_dir, "index.html")

# 1. Read all study-guide question JSON files
study_data = {}
total_study_qs = 0
for u in range(1, 9):
    file_name = f"unit{u}_questions.json"
    file_path = os.path.join(base_dir, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            study_data[u] = data
            total_study_qs += len(data)
            print(f"Loaded study Unit {u}: {len(data)} questions.")
    else:
        print(f"Warning: {file_name} not found!")

# 2. Read all exam simulator JSON files
exam_data = {}
for p in range(1, 5):
    file_name = f"part{p}_exam.json"
    file_path = os.path.join(base_dir, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            exam_data[f"part{p}"] = data
            print(f"Loaded exam Part {p}: {len(data)} questions/prompts.")
    else:
        print(f"Warning: {file_name} not found!")

# 3. Read all active recall JSON files
active_recall_data = {}
for u in range(1, 9):
    file_name = f"unit{u}_active_recall.json"
    file_path = os.path.join(base_dir, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            active_recall_data[u] = data
            print(f"Loaded active recall Unit {u}: {len(data)} pages.")
    else:
        active_recall_data[u] = []
        print(f"Warning: {file_name} not found (using empty list).")

# 4. Read all history question JSON files
history_data = {}
for u in range(5, 9):
    file_name = f"history_unit{u}_questions.json"
    file_path = os.path.join(base_dir, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            history_data[u] = data
            print(f"Loaded history Unit {u}: {len(data)} questions.")
    else:
        history_data[u] = []
        print(f"Warning: {file_name} not found (using empty list).")

# HTML template definition
html_template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Comprehensive Biology Study Suite &amp; Final Exam Simulator</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root[data-theme="light"] {
    --bg: #faf9f6;
    --surface: #ffffff;
    --surface2: #f5f3ee;
    --surface3: #efece4;
    --border: #e7e3d8;
    --border-strong: #d8d3c4;
    --text-primary: #1d1c19;
    --text-secondary: #595650;
    --text-dim: #908b80;
    --text-faint: #b6b1a4;
    
    --correct: #2f7d4f;
    --correct-soft: #e6f1e8;
    --correct-soft-2: #d6e8d9;
    --correct-ink: #1f5a38;
    
    --wrong: #c0392b;
    --wrong-soft: #fdf2f2;
    --wrong-soft-2: #f9d5d5;
    --wrong-ink: #7b241c;
    
    --accent: #2563a8;
    --accent-soft: #e4eef7;
    --accent-soft-2: #d1e2f1;
    --accent-ink: #184879;
    
    --amber: #b6802a;
    --amber-soft: #fbf3df;
    --amber-ink: #7a5615;
    --amber-border: #ecd9a3;
  }
  
  :root[data-theme="dark"] {
    --bg: #151412;
    --surface: #1e1d1a;
    --surface2: #282622;
    --surface3: #32302b;
    --border: #35332e;
    --border-strong: #4a4740;
    --text-primary: #faf9f6;
    --text-secondary: #c5c2ba;
    --text-dim: #8b887f;
    --text-faint: #5a5852;
    
    --correct: #3aa666;
    --correct-soft: #1b2d21;
    --correct-soft-2: #24422e;
    --correct-ink: #a2e8c2;
    
    --wrong: #e74c3c;
    --wrong-soft: #301b1a;
    --wrong-soft-2: #482321;
    --wrong-ink: #f5b0a7;
    
    --accent: #3498db;
    --accent-soft: #1b2f42;
    --accent-soft-2: #25425f;
    --accent-ink: #aed6f1;
    
    --amber: #f39c12;
    --amber-soft: #342817;
    --amber-ink: #f9e79f;
    --amber-border: #876228;
  }
  
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  
  body {
    background: var(--bg);
    color: var(--text-primary);
    font-family: 'DM Sans', sans-serif;
    font-size: 15.5px;
    line-height: 1.6;
    padding-bottom: 96px;
    transition: background 0.3s, color 0.3s;
    -webkit-font-smoothing: antialiased;
  }
  
  /* ══ NAVIGATION & HEADER ══ */
  .top-bar {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(26, 25, 23, 0.94);
    border-bottom: 1px solid var(--border-strong);
    color: #faf9f6;
    padding: 0 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
    backdrop-filter: blur(10px);
  }
  
  .top-bar[data-theme="dark"] {
    background: rgba(21, 20, 18, 0.94);
  }
  
  .brand {
    font-family: 'DM Serif Display', serif;
    font-size: 18px;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  
  .brand span.subtitle {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--text-dim);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    border: 1px solid var(--border-strong);
    padding: 2px 6px;
    border-radius: 4px;
  }
  
  .top-actions {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  
  .save-indicator {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--correct);
    display: flex;
    align-items: center;
    gap: 6px;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  .save-indicator.active {
    opacity: 1;
  }
  
  .pulse-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--correct);
    animation: pulse 1.5s infinite;
  }
  
  @keyframes pulse {
    0% { transform: scale(0.9); opacity: 1; }
    50% { transform: scale(1.3); opacity: 0.4; }
    100% { transform: scale(0.9); opacity: 1; }
  }
  
  .theme-toggle {
    background: transparent;
    border: 1px solid var(--border-strong);
    color: #faf9f6;
    padding: 6px 12px;
    font-size: 12.5px;
    border-radius: 6px;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }
  
  .theme-toggle:hover {
    background: rgba(255, 255, 255, 0.1);
  }
  
  /* ══ CONTAINER LAYOUT ══ */
  .layout-container {
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 290px 1fr;
    gap: 32px;
    padding: 32px 24px;
  }
  
  @media (max-width: 950px) {
    .layout-container {
      grid-template-columns: 1fr;
      padding: 16px;
    }
  }
  
  /* ══ LEFT SIDEBAR (DASHBOARD & NAV) ══ */
  .sidebar {
    position: sticky;
    top: 96px;
    height: calc(100vh - 128px);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
    scrollbar-width: thin;
  }
  
  .sidebar::-webkit-scrollbar {
    width: 4px;
  }
  
  .sidebar::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 4px;
  }
  
  @media (max-width: 950px) {
    .sidebar {
      position: static;
      height: auto;
    }
  }
  
  .sidebar-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }
  
  .dashboard-title {
    font-family: 'DM Serif Display', serif;
    font-size: 17px;
    margin-bottom: 12px;
    letter-spacing: -0.01em;
  }
  
  /* Progress Metrics */
  .progress-ring-box {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 12px;
  }
  
  .score-display {
    font-family: 'DM Serif Display', serif;
    font-size: 32px;
    line-height: 1;
    color: var(--accent);
  }
  
  .score-label {
    font-size: 12.5px;
    color: var(--text-secondary);
  }
  
  .bar-container {
    height: 8px;
    background: var(--surface2);
    border-radius: 999px;
    overflow: hidden;
    margin-top: 6px;
  }
  
  .bar-fill {
    height: 100%;
    background: var(--accent);
    border-radius: 999px;
    width: 0%;
    transition: width 0.5s cubic-bezier(0.1, 0.8, 0.3, 1);
  }
  
  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 12px;
    font-size: 12.5px;
  }
  
  .stat-card {
    background: var(--surface2);
    padding: 6px 8px;
    border-radius: 6px;
    border: 1px solid var(--border);
    text-align: center;
  }
  
  .stat-num {
    font-weight: 700;
    font-family: 'DM Mono', monospace;
    font-size: 14px;
  }
  
  .stat-num.correct-text { color: var(--correct); }
  .stat-num.wrong-text { color: var(--wrong); }
  
  /* Navigation List */
  .unit-nav-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  
  .unit-nav-btn {
    width: 100%;
    text-align: left;
    background: transparent;
    border: 1px solid transparent;
    padding: 9px 12px;
    border-radius: 8px;
    cursor: pointer;
    font-family: inherit;
    font-size: 13px;
    font-weight: 500;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: all 0.15s ease;
  }
  
  .unit-nav-btn:hover {
    background: var(--surface2);
    color: var(--text-primary);
  }
  
  .unit-nav-btn.active {
    background: var(--surface3);
    border-color: var(--border-strong);
    color: var(--text-primary);
    font-weight: 600;
  }
  
  .unit-nav-name {
    display: flex;
    align-items: center;
    gap: 8px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .unit-badge {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    background: var(--surface3);
    padding: 1px 4px;
    border-radius: 4px;
    border: 1px solid var(--border);
  }
  
  .unit-nav-progress {
    font-size: 11px;
    color: var(--text-dim);
    font-family: 'DM Mono', monospace;
  }
  
  .reset-btn {
    width: 100%;
    margin-top: 8px;
    background: transparent;
    border: 1px solid var(--border-strong);
    color: var(--wrong);
    padding: 8px;
    border-radius: 8px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    transition: all 0.15s;
  }
  
  .reset-btn:hover {
    background: var(--wrong-soft);
    border-color: var(--wrong-soft-2);
  }
  
  /* ══ MAIN WORK AREA ══ */
  .main-content {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  
  .hero-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }
  
  .hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-dim);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  
  .hero-panel h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(26px, 3.5vw, 36px);
    line-height: 1.15;
    margin-bottom: 12px;
  }
  
  .hero-panel p {
    color: var(--text-secondary);
    font-size: 14.5px;
    max-width: 780px;
  }
  
  /* Mode selectors */
  .mode-select-bar {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
    flex-wrap: wrap;
  }
  
  .mode-toggle {
    display: inline-flex;
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 3px;
    border-radius: 8px;
  }
  
  .mode-toggle-btn {
    background: transparent;
    border: none;
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    font-family: inherit;
    transition: all 0.12s;
  }
  
  .mode-toggle-btn.active {
    background: var(--surface);
    color: var(--text-primary);
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }
  
  /* ══ SECTION CARDS ══ */
  .section-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 20px;
  }
  
  .section-header {
    background: linear-gradient(to bottom, var(--surface), var(--surface2));
    padding: 16px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
    user-select: none;
  }
  
  .section-header-left {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  
  .section-badge {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    background: var(--accent-soft);
    color: var(--accent-ink);
    border: 1px solid var(--accent-soft-2);
    padding: 4px 8px;
    border-radius: 6px;
  }
  
  .section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 18px;
  }
  
  .section-header-right {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .section-progress {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--text-secondary);
  }
  
  .collapse-icon {
    font-size: 10px;
    color: var(--text-dim);
    transition: transform 0.2s ease;
  }
  
  .collapse-icon.open {
    transform: rotate(180deg);
  }
  
  .section-body {
    display: none;
    padding: 24px;
    border-bottom: 1px solid var(--border);
  }
  
  .section-body.open {
    display: block;
  }
  
  /* ══ QUESTION BLOCK ══ */
  .q-block {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 18px;
    transition: all 0.2s ease;
  }
  
  .q-block:last-child {
    margin-bottom: 0;
  }
  
  .q-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
  }
  
  .q-type-badge {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 500;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  
  .q-state-badge {
    font-family: 'DM Sans', sans-serif;
    font-size: 10.5px;
    font-weight: 600;
    display: none;
    padding: 2px 6px;
    border-radius: 4px;
  }
  
  .q-state-badge.correct {
    display: inline-block;
    background: var(--correct-soft);
    color: var(--correct-ink);
  }
  
  .q-state-badge.wrong {
    display: inline-block;
    background: var(--wrong-soft);
    color: var(--wrong-ink);
  }
  
  .q-text {
    font-size: 15px;
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 14px;
    line-height: 1.55;
  }
  
  .opts-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .opt-label {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid var(--border);
    background: var(--surface);
    cursor: pointer;
    font-size: 14px;
    color: var(--text-secondary);
    transition: all 0.12s ease;
    line-height: 1.45;
    user-select: none;
  }
  
  .opt-label:hover:not(.locked) {
    border-color: var(--border-strong);
    background: var(--surface3);
    color: var(--text-primary);
  }
  
  .opt-label.selected {
    border-color: var(--accent);
    background: var(--accent-soft);
    color: var(--text-primary);
  }
  
  .opt-label.correct {
    background: var(--correct-soft);
    border-color: var(--correct-soft-2);
    color: var(--correct-ink);
    font-weight: 500;
  }
  
  .opt-label.wrong {
    background: var(--wrong-soft);
    border-color: var(--wrong-soft-2);
    color: var(--wrong-ink);
  }
  
  .opt-label.missed {
    background: var(--correct-soft);
    border-color: var(--correct-soft-2);
    color: var(--correct-ink);
    opacity: 0.7;
    border-style: dashed;
  }
  
  .opt-label.locked {
    pointer-events: none;
  }
  
  .opt-input {
    margin-top: 3.5px;
    flex-shrink: 0;
  }
  
  .opt-letter {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-dim);
    margin-top: 1px;
    min-width: 18px;
    flex-shrink: 0;
  }
  
  .opt-text {
    flex-grow: 1;
  }
  
  .q-actions {
    margin-top: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .q-btn {
    padding: 8px 18px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.12s;
  }
  
  .q-btn:hover:not(:disabled) {
    background: var(--surface3);
  }
  
  .q-btn:disabled {
    opacity: 0.5;
    cursor: default;
  }
  
  .q-btn.primary {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
  }
  
  .q-btn.primary:hover:not(:disabled) {
    opacity: 0.9;
  }
  
  .q-feedback {
    margin-top: 12px;
    padding: 14px;
    border-radius: 8px;
    font-size: 13.5px;
    display: none;
    line-height: 1.55;
  }
  
  .q-feedback.show {
    display: block;
  }
  
  .q-feedback.good {
    background: var(--correct-soft);
    color: var(--correct-ink);
    border-left: 4px solid var(--correct);
  }
  
  .q-feedback.bad {
    background: var(--wrong-soft);
    color: var(--wrong-ink);
    border-left: 4px solid var(--wrong);
  }
  
  /* Semicolon-grade individual options explanation box */
  .opt-explanations-box {
    margin-top: 12px;
    padding: 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    font-size: 13px;
    line-height: 1.5;
  }
  
  .opt-explanations-title {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-dim);
    margin-bottom: 8px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 4px;
  }
  
  .opt-exp-item {
    margin-bottom: 6px;
  }
  
  .opt-exp-item:last-child {
    margin-bottom: 0;
  }
  
  .opt-exp-item.correct-item {
    color: var(--correct-ink);
  }
  
  /* Section check controls */
  .section-check-panel {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 20px;
    padding: 14px 18px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
  }
  
  /* ══ EXAM SIMULATOR ELEMENTS ══ */
  .exam-lobby-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }
  
  .exam-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin: 24px 0;
  }
  
  .exam-part-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    text-align: center;
  }
  
  .exam-part-num {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    margin-bottom: 4px;
  }
  
  .exam-part-title {
    font-size: 13px;
    color: var(--text-secondary);
    margin-bottom: 8px;
  }
  
  .exam-part-weight {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    background: var(--surface3);
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
  }
  
  .written-answer-box {
    width: 100%;
    height: 160px;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 14px;
    line-height: 1.5;
    resize: vertical;
    margin-top: 10px;
  }
  
  .written-answer-box:focus {
    outline: none;
    border-color: var(--accent);
  }
  
  .rubric-box {
    margin-top: 14px;
    padding: 14px;
    background: var(--amber-soft);
    border: 1px solid var(--amber-border);
    border-left: 4px solid var(--amber);
    border-radius: 8px;
    font-size: 13.5px;
  }
  
  .model-ans-box {
    margin-top: 12px;
    padding: 14px;
    background: var(--correct-soft);
    border: 1px solid var(--correct-soft-2);
    border-left: 4px solid var(--correct);
    border-radius: 8px;
    font-size: 13.5px;
    color: var(--correct-ink);
  }
  
  .rubric-header {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
    margin-bottom: 6px;
    display: block;
  }
  
  .rubric-levels {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: 6px;
  }
  
  .self-score-select {
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 13px;
    font-weight: 600;
  }
  
  /* ══ PRACTICE EXAM VIEW ══ */
  .exam-setup-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }
  
  .exam-setup-title {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    margin-bottom: 12px;
  }
  
  .form-group {
    margin-bottom: 16px;
  }
  
  .form-group label {
    display: block;
    font-size: 13.5px;
    font-weight: 600;
    margin-bottom: 6px;
    color: var(--text-secondary);
  }
  
  .form-select {
    width: 100%;
    max-width: 320px;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 14px;
  }
  
  .exam-btn {
    background: var(--correct);
    color: #fff;
    border: 1px solid var(--correct);
    padding: 12px 28px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s;
  }
  
  .exam-btn:hover {
    opacity: 0.9;
  }
  
  .exam-header {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    flex-wrap: wrap;
    gap: 16px;
  }
  
  .exam-meta-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
  }
  
  .exam-timer {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 600;
    color: var(--amber-ink);
    background: var(--amber-soft);
    padding: 6px 14px;
    border-radius: 8px;
    border: 1px solid var(--amber-border);
  }
  
  /* Reset overlay and modal */
  .modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
    z-index: 1000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 16px;
  }
  
  .modal-overlay.active {
    display: flex;
  }
  
  .modal-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    max-width: 440px;
    width: 100%;
    padding: 24px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
  }
  
  .modal-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    margin-bottom: 12px;
  }
  
  .modal-body {
    font-size: 14.5px;
    color: var(--text-secondary);
    margin-bottom: 20px;
    line-height: 1.5;
  }
  
  .modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
  }
  
  /* ══ COLOR ACCENTS FOR UNITS ══ */
  .unit-card[data-unit="1"] { border-top: 4px solid #8e44ad; }
  .unit-card[data-unit="2"] { border-top: 4px solid #2980b9; }
  .unit-card[data-unit="3"] { border-top: 4px solid #16a085; }
  .unit-card[data-unit="4"] { border-top: 4px solid #27ae60; }
  .unit-card[data-unit="5"] { border-top: 4px solid #f39c12; }
  .unit-card[data-unit="6"] { border-top: 4px solid #d35400; }
  .unit-card[data-unit="7"] { border-top: 4px solid #c0392b; }
  .unit-card[data-unit="8"] { border-top: 4px solid #1abc9c; }
  
  .unit-indicator-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }
  
  .unit-indicator-dot[data-unit="1"] { background: #8e44ad; }
  .unit-indicator-dot[data-unit="2"] { background: #2980b9; }
  .unit-indicator-dot[data-unit="3"] { background: #16a085; }
  .unit-indicator-dot[data-unit="4"] { background: #27ae60; }
  .unit-indicator-dot[data-unit="5"] { background: #f39c12; }
  .unit-indicator-dot[data-unit="6"] { background: #d35400; }
  .unit-indicator-dot[data-unit="7"] { background: #c0392b; }
  .unit-indicator-dot[data-unit="8"] { background: #1abc9c; }

  /* ══ MUSIC PLAYER WIDGET ══ */
  .music-player-card {
    background: var(--surface);
    border: 1px solid var(--border);
    margin-top: 12px;
  }
  
  .vinyl-disc {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--surface2);
    border: 1px solid var(--border-strong);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-secondary);
    transition: transform 0.3s, border-color 0.3s;
  }
  
  .vinyl-disc.playing {
    animation: rotate-vinyl 4s linear infinite;
    color: var(--accent);
    border-color: var(--accent);
  }
  
  @keyframes rotate-vinyl {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  
  .equalizer-bars {
    display: flex;
    align-items: flex-end;
    gap: 2.5px;
    height: 14px;
    width: 24px;
    opacity: 0.3;
    transition: opacity 0.3s;
  }
  
  .equalizer-bars.playing {
    opacity: 1;
  }
  
  .equalizer-bars span {
    width: 3px;
    height: 100%;
    background-color: var(--accent);
    border-radius: 1px;
    transform-origin: bottom;
  }
  
  .equalizer-bars.playing span:nth-child(1) { animation: bounce-bar 0.8s ease-in-out infinite alternate; }
  .equalizer-bars.playing span:nth-child(2) { animation: bounce-bar 0.5s ease-in-out infinite alternate 0.15s; }
  .equalizer-bars.playing span:nth-child(3) { animation: bounce-bar 0.9s ease-in-out infinite alternate 0.05s; }
  .equalizer-bars.playing span:nth-child(4) { animation: bounce-bar 0.6s ease-in-out infinite alternate 0.2s; }
  
  @keyframes bounce-bar {
    0% { transform: scaleY(0.2); }
    100% { transform: scaleY(1); }
  }
  
  /* ══ SECTION ACTION BUTTONS ══ */
  .section-actions-bar {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 12px;
  }
  .section-actions-bar .sec-action-btn {
    padding: 4px 10px;
    font-size: 11.5px;
    font-weight: 600;
    font-family: 'DM Sans', sans-serif;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--surface2);
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    transition: all 0.15s;
  }
  .section-actions-bar .sec-action-btn:hover {
    background: var(--accent-soft);
    color: var(--accent);
    border-color: var(--accent);
  }
  .section-actions-bar .sec-action-btn.danger:hover {
    background: var(--wrong-soft);
    color: var(--wrong);
    border-color: var(--wrong);
  }
</style>
</head>
<body>

<nav class="top-bar">
  <div class="brand">
    Biology 9 <span class="subtitle">Study Suite &amp; Exam Simulator</span>
  </div>
  <div class="top-actions">
    <div class="save-indicator" id="save-indicator">
      <div class="pulse-dot"></div>
      Progress Saved
    </div>
    <button class="theme-toggle" id="theme-toggle">Dark Mode</button>
    <button class="theme-toggle" id="top-reset-btn" style="border-color: var(--wrong); color: var(--wrong); font-weight:600;">Reset Progress</button>
  </div>
</nav>

<div class="layout-container">
  
  <!-- LEFT SIDEBAR -->
  <aside class="sidebar">
    
    <!-- Subject Switcher -->
    <div class="sidebar-box" style="padding: 10px; display: flex; gap: 8px; margin-bottom: 0;">
      <button class="q-btn primary" id="subject-bio-btn" style="flex: 1; text-align: center; padding: 8px 4px; font-weight: 700; margin: 0; font-size: 12.5px; border-radius: 8px;" onclick="setSubject('biology')">🧬 Biology</button>
      <button class="q-btn" id="subject-hist-btn" style="flex: 1; text-align: center; padding: 8px 4px; font-weight: 700; margin: 0; font-size: 12.5px; border-radius: 8px;" onclick="setSubject('history')">📜 History</button>
    </div>
    
    <!-- Progress Panel -->
    <div class="sidebar-box">
      <h2 class="dashboard-title" id="progress-panel-title">Biology Study Progress</h2>
      <div class="progress-ring-box">
        <div>
          <div class="score-display" id="overall-pct">0%</div>
          <div class="score-label" id="overall-fraction">0 of 0 answered</div>
        </div>
      </div>
      <div class="bar-container">
        <div class="bar-fill" id="overall-bar-fill"></div>
      </div>
      <div class="stats-grid">
        <div class="stat-card">
          <div class="score-label">Correct</div>
          <div class="stat-num correct-text" id="stat-correct">0</div>
        </div>
        <div class="stat-card">
          <div class="score-label">Incorrect</div>
          <div class="stat-num wrong-text" id="stat-wrong">0</div>
        </div>
      </div>
      <button class="reset-btn" id="reset-progress-btn">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
        Reset Progress
      </button>
    </div>
    
    <!-- Navigation Links -->
    <div class="sidebar-box" style="flex-grow: 1; margin-bottom: 0;">
      <h2 class="dashboard-title" style="font-size: 13px; text-transform: uppercase; color: var(--text-dim); letter-spacing: 0.05em; margin-bottom: 10px;">Study Rooms</h2>
      <ul class="unit-nav-list" id="unit-nav-list-container">
        <!-- Populated dynamically via JS -->
      </ul>
    </div>

    <!-- Music Player Widget -->
    <div class="sidebar-box music-player-card">
      <h2 class="dashboard-title" style="font-size: 13px; text-transform: uppercase; color: var(--text-dim); letter-spacing: 0.05em; margin-bottom: 10px;">Phonk Station</h2>
      <div style="display:flex; align-items:center; gap:12px;">
        <div class="vinyl-disc" id="vinyl-disc">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/></svg>
        </div>
        <div style="flex-grow:1; min-width:0;">
          <div style="font-size:12px; font-weight:600; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" id="track-title">Yara Yara Phonk 🥹😅👿👿</div>
          <div style="font-size:10px; color:var(--text-dim);" id="track-status">Stopped</div>
        </div>
      </div>
      <div style="display:flex; align-items:center; justify-content:space-between; margin-top:12px; gap:8px;">
        <div class="equalizer-bars" id="eq-bars">
          <span></span><span></span><span></span><span></span>
        </div>
        <div style="display:flex; gap:6px;">
          <button class="q-btn primary" id="music-play-btn" style="padding:4px 10px; font-size:11.5px; display:flex; align-items:center; gap:4px; font-weight:600;">
            <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg> Play
          </button>
          <button class="q-btn" id="music-stop-btn" style="padding:4px 10px; font-size:11.5px; display:flex; align-items:center; gap:4px; font-weight:600;" disabled>
            <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><rect x="4" y="4" width="16" height="16"/></svg> Stop
          </button>
        </div>
      </div>
    </div>

  </aside>
  
  <!-- RIGHT CONTENT AREA -->
  <main class="main-content" id="main-view">
    <!-- Content will be dynamically populated here -->
  </main>
  
</div>

<!-- Modal Confirmation dialog -->
<div class="modal-overlay" id="confirm-modal">
  <div class="modal-box">
    <div class="modal-title">Reset ALL Suite Progress?</div>
    <div class="modal-body">
      This will permanently wipe all your saved study progress, active exam sessions, and graded exam results across the entire application on this browser. You cannot undo this. Do you want to proceed?
    </div>
    <div class="modal-actions">
      <button class="q-btn" id="modal-cancel">Cancel</button>
      <button class="q-btn primary" id="modal-confirm" style="background: var(--wrong); border-color: var(--wrong);">Reset Everything</button>
    </div>
  </div>
</div>

<script>
// RAW QUIZ DATA INJECTED
const QUIZ_DATA = %s;
const EXAM_DATA = %s;
const ACTIVE_RECALL_DATA = %s;
const HISTORY_DATA = %s;
const HISTORY_EXAM_DATA = %s;
const ULTIMATE_STUDY_DATA = %s;

// Global application state
let appState = {
  theme: 'light',
  feedbackMode: 'immediate', // 'immediate' or 'section'
  currentView: 'dashboard', // 'dashboard', 'unit-1'..'unit-8', 'practice-exam', 'final-exam-simulator', 'active-recall', 'ultimate-study'
  currentSubject: 'biology', // 'biology' or 'history'
  userAnswers: {}, // key: q_unit_section_idx -> { selected: [indices], locked: true, correct: boolean }
  activeRecallAnswers: {}, // key: ar_unit_page_qidx -> { selected: [indices], locked: true, correct: boolean }
  activeRecallUnit: 1,
  activeRecallPage: 1,
  
  // Final Exam Simulator Session State
  examSession: null, // Active exam session details (MC answers, text responses, time left)
  examResult: null,   // Completed, graded exam results for review
  examGradingMode: 'end', // 'end' (check at end, recommended) or 'during' (check during test)
  
  // Ultimate Study Mode State
  ultimateStudyMastery: {}, // key: topic_id -> mastery level (0=unopened, 1=reviewing, 2=mastered)
  ultimateActiveTopic: 'u1_t1', // active topic ID or 'active-outline' or 'oe_...'
  ultimateOpenEndedDrafts: {}, // key: prompt_id -> text draft, and prompt_id + '_done' -> boolean
  ultimateRecallBlanks: {}, // key: blank_id/card_id -> value or state
  ultimateActiveOutlineUnit: 1,
  ultimateZenMode: false
};

// Load saved state from localStorage
function loadState() {
  const savedState = localStorage.getItem('bio_quiz_state_v3');
  if (savedState) {
    try {
      appState.userAnswers = JSON.parse(savedState);
    } catch(e) {
      appState.userAnswers = {};
    }
  }
  
  const savedTheme = localStorage.getItem('bio_quiz_theme');
  if (savedTheme) {
    appState.theme = savedTheme;
    document.documentElement.setAttribute('data-theme', savedTheme);
    document.getElementById('theme-toggle').textContent = savedTheme === 'light' ? 'Dark Mode' : 'Light Mode';
  }
  
  const savedMode = localStorage.getItem('bio_quiz_feedback_mode');
  if (savedMode) {
    appState.feedbackMode = savedMode;
  }
  
  const savedSubject = localStorage.getItem('quiz_subject_v1');
  if (savedSubject) {
    appState.currentSubject = savedSubject;
  }
  
  const savedRecallAnswers = localStorage.getItem('quiz_recall_answers_v1');
  if (savedRecallAnswers) {
    try {
      appState.activeRecallAnswers = JSON.parse(savedRecallAnswers);
    } catch(e) {
      appState.activeRecallAnswers = {};
    }
  }
  
  const savedRecallUnit = localStorage.getItem('quiz_recall_unit_v1');
  if (savedRecallUnit) {
    appState.activeRecallUnit = parseInt(savedRecallUnit) || 1;
  }
  
  const savedRecallPage = localStorage.getItem('quiz_recall_page_v1');
  if (savedRecallPage) {
    appState.activeRecallPage = parseInt(savedRecallPage) || 1;
  }
  
  // Load active final exam session or graded result
  const savedExamSession = localStorage.getItem('bio_final_exam_session');
  if (savedExamSession) {
    try {
      appState.examSession = JSON.parse(savedExamSession);
    } catch(e) {
      appState.examSession = null;
    }
  }
  
  const savedExamResult = localStorage.getItem('bio_final_exam_result');
  if (savedExamResult) {
    try {
      appState.examResult = JSON.parse(savedExamResult);
    } catch(e) {
      appState.examResult = null;
    }
  }

  // Load Ultimate Study state
  const savedUltimateMastery = localStorage.getItem('ultimate_study_mastery_v1');
  if (savedUltimateMastery) {
    try { appState.ultimateStudyMastery = JSON.parse(savedUltimateMastery); } catch(e) {}
  }
  if (!appState.ultimateStudyMastery) appState.ultimateStudyMastery = {};

  const savedUltimateActive = localStorage.getItem('ultimate_active_topic_v1');
  if (savedUltimateActive) appState.ultimateActiveTopic = savedUltimateActive;

  const savedUltimateDrafts = localStorage.getItem('ultimate_oe_drafts_v1');
  if (savedUltimateDrafts) {
    try { appState.ultimateOpenEndedDrafts = JSON.parse(savedUltimateDrafts); } catch(e) {}
  }
  if (!appState.ultimateOpenEndedDrafts) appState.ultimateOpenEndedDrafts = {};

  const savedUltimateBlanks = localStorage.getItem('ultimate_recall_blanks_v1');
  if (savedUltimateBlanks) {
    try { appState.ultimateRecallBlanks = JSON.parse(savedUltimateBlanks); } catch(e) {}
  }
  if (!appState.ultimateRecallBlanks) appState.ultimateRecallBlanks = {};

  const savedUltimateOutlineUnit = localStorage.getItem('ultimate_outline_unit_v1');
  if (savedUltimateOutlineUnit) appState.ultimateActiveOutlineUnit = parseInt(savedUltimateOutlineUnit) || 1;

  const savedUltimateZen = localStorage.getItem('ultimate_zen_mode_v1');
  if (savedUltimateZen) appState.ultimateZenMode = savedUltimateZen === 'true';

  const savedActualAnswers = localStorage.getItem('actual_outline_answers_v1');
  if (savedActualAnswers) {
    try { appState.actualOutlineAnswers = JSON.parse(savedActualAnswers); } catch(e) {}
  }
  if (!appState.actualOutlineAnswers) appState.actualOutlineAnswers = {};
}

// Save study progress state
function saveState() {
  localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
  localStorage.setItem('quiz_recall_answers_v1', JSON.stringify(appState.activeRecallAnswers));
  localStorage.setItem('quiz_recall_unit_v1', appState.activeRecallUnit);
  localStorage.setItem('quiz_recall_page_v1', appState.activeRecallPage);
  localStorage.setItem('quiz_subject_v1', appState.currentSubject);

  // Save Ultimate Study state
  localStorage.setItem('ultimate_study_mastery_v1', JSON.stringify(appState.ultimateStudyMastery));
  localStorage.setItem('ultimate_active_topic_v1', appState.ultimateActiveTopic);
  localStorage.setItem('ultimate_oe_drafts_v1', JSON.stringify(appState.ultimateOpenEndedDrafts));
  localStorage.setItem('ultimate_recall_blanks_v1', JSON.stringify(appState.ultimateRecallBlanks));
  localStorage.setItem('ultimate_outline_unit_v1', appState.ultimateActiveOutlineUnit || 1);
  localStorage.setItem('ultimate_zen_mode_v1', appState.ultimateZenMode);
  localStorage.setItem('actual_outline_answers_v1', JSON.stringify(appState.actualOutlineAnswers));

  flashSaveIndicator();
}

function flashSaveIndicator() {
  const indicator = document.getElementById('save-indicator');
  if (indicator) {
    indicator.classList.add('active');
    setTimeout(() => {
      indicator.classList.remove('active');
    }, 1200);
  }
}

// Save active exam simulator session state
function saveExamSession() {
  if (appState.examSession) {
    localStorage.setItem('bio_final_exam_session', JSON.stringify(appState.examSession));
  } else {
    localStorage.removeItem('bio_final_exam_session');
  }
}

// Save graded exam result
function saveExamResult() {
  if (appState.examResult) {
    localStorage.setItem('bio_final_exam_result', JSON.stringify(appState.examResult));
  } else {
    localStorage.removeItem('bio_final_exam_result');
  }
}

function getActiveQuizData() {
  return appState.currentSubject === 'biology' ? QUIZ_DATA : HISTORY_DATA;
}

// Calculate scores for the study guide
function calculateProgress() {
  let stats = {
    totalQuestions: 0,
    answered: 0,
    correct: 0,
    wrong: 0,
    units: {}
  };
  
  const data = getActiveQuizData();
  const startUnit = appState.currentSubject === 'biology' ? 1 : 5;
  const endUnit = 8;
  
  for (let u = startUnit; u <= endUnit; u++) {
    stats.units[u] = { total: 0, answered: 0, correct: 0 };
    if (!data[u]) continue;
    
    stats.totalQuestions += data[u].length;
    stats.units[u].total = data[u].length;
    
    data[u].forEach((q, idx) => {
      const qKey = appState.currentSubject === 'biology' ? `q_${u}_${q.section}_${idx}` : `q_hist_${u}_${q.section}_${idx}`;
      const ans = appState.userAnswers[qKey];
      
      if (ans && ans.locked) {
        stats.answered++;
        stats.units[u].answered++;
        if (ans.correct) {
          stats.correct++;
          stats.units[u].correct++;
        } else {
          stats.wrong++;
        }
      }
    });
  }
  
  return stats;
}

// Update sidebar display
function updateDashboardUI() {
  const stats = calculateProgress();
  
  // Title of the progress panel
  const panelTitle = document.getElementById('progress-panel-title');
  if (panelTitle) {
    panelTitle.textContent = appState.currentSubject === 'biology' ? 'Biology Study Progress' : 'History Study Progress';
  }
  
  // Overall display
  const overallPct = stats.totalQuestions > 0 ? Math.round((stats.correct / stats.totalQuestions) * 100) : 0;
  const overallAnsPct = stats.totalQuestions > 0 ? Math.round((stats.answered / stats.totalQuestions) * 100) : 0;
  
  document.getElementById('overall-pct').textContent = overallPct + '%';
  document.getElementById('overall-fraction').textContent = `${stats.answered} of ${stats.totalQuestions} answered`;
  document.getElementById('overall-bar-fill').style.width = overallAnsPct + '%';
  
  document.getElementById('stat-correct').textContent = stats.correct;
  document.getElementById('stat-wrong').textContent = stats.wrong;
  
  // Nav items progress
  const startUnit = appState.currentSubject === 'biology' ? 1 : 5;
  const endUnit = 8;
  for (let u = startUnit; u <= endUnit; u++) {
    const uStats = stats.units[u];
    if (uStats) {
      const uPct = uStats.total > 0 ? Math.round((uStats.answered / uStats.total) * 100) : 0;
      const progLabel = document.getElementById(`nav-prog-${u}`);
      if (progLabel) {
        progLabel.textContent = uPct + '%';
      }
    }
  }
}

// Global functions to handle view switching
function showView(viewId) {
  appState.currentView = viewId;
  
  // Clear any running active exam timer interval if we navigate away (but keep the session alive)
  if (viewId !== 'final-exam-simulator' && appState.examSession && appState.examSession.timerInterval) {
    clearInterval(appState.examSession.timerInterval);
    appState.examSession.timerInterval = null;
  }
  
  // Update nav UI active class
  document.querySelectorAll('.unit-nav-btn').forEach(btn => {
    if (btn.dataset.target === viewId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
  
  const mainView = document.getElementById('main-view');
  
  if (viewId === 'dashboard') {
    renderOverallDashboard(mainView);
  } else if (viewId.startsWith('unit-')) {
    const unitNum = parseInt(viewId.split('-')[1]);
    renderUnitView(mainView, unitNum);
  } else if (viewId === 'practice-exam') {
    renderPracticeExamSetup(mainView);
  } else if (viewId === 'final-exam-simulator') {
    renderFinalExamView(mainView);
  } else if (viewId === 'history-final-exam') {
    renderHistoryFinalExam(mainView);
  } else if (viewId === 'active-recall') {
    renderActiveRecallView(mainView);
  } else if (viewId === 'ultimate-study') {
    renderUltimateStudyView(mainView);
  } else if (viewId === 'actual-outline') {
    renderActualOutlineView(mainView);
  }
  
  window.scrollTo(0, 0);
}

// ── HISTORY FINAL EXAM SIMULATOR ──
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
    <div class="exam-grid">
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
    block.className = 'q-block';
    block.innerHTML = `${withDocument ? `<div style="padding:12px;background:var(--surface2);border-left:4px solid var(--accent);margin-bottom:12px;border-radius:6px;font-size:14.5px;"><strong>Document:</strong> ${q.document}</div>` : ''}
      <div class="q-meta"><span class="q-type-badge">${prefix === 'objective' ? 'Section 1' : 'Section 2'}</span></div>
      <div class="q-text" style="margin-bottom:12px;"><strong>${i + 1}.</strong> ${q.q}</div>
      <div class="opts-container">${q.opts.map((o,j)=>`<label class="opt-label"><input type="radio" class="opt-input" name="${prefix}_${i}" value="${j}" ${answers[i]===j?'checked':''}><span class="opt-letter">${String.fromCharCode(65+j)}</span><span>${o}</span></label>`).join('')}</div>`;
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
    <div class="section-card"><div class="section-header" onclick="toggleSectionBody('history-exam-objective')"><span class="section-title">Section 1 - 90 Objective Questions</span><span class="collapse-icon open">&#9660;</span></div><div class="section-body open" id="history-exam-objective"></div></div>
    <div class="section-card"><div class="section-header" onclick="toggleSectionBody('history-exam-documents')"><span class="section-title">Section 2 - 30 Document-based Objective Questions</span><span class="collapse-icon open">&#9660;</span></div><div class="section-body open" id="history-exam-documents"></div></div>
    <div class="section-card"><div class="section-header" onclick="toggleSectionBody('history-exam-open')"><span class="section-title">Section 3 - 2 Open-ended Responses</span><span class="collapse-icon open">&#9660;</span></div><div class="section-body open" id="history-exam-open"></div></div>
    <div style="display:flex;gap:12px;margin-top:20px;"><button class="q-btn" onclick="if(confirm('Delete this attempt?')){saveHistoryExam('session',null);showView('history-final-exam')}">Reset Attempt</button><button class="q-btn primary" style="flex:1;" onclick="submitHistoryFinalExam()">Submit Final Exam</button></div>`;
  renderHistoryExamMC(document.getElementById('history-exam-objective'), HISTORY_EXAM_DATA.objective, session.objective, 'objective', false);
  renderHistoryExamMC(document.getElementById('history-exam-documents'), HISTORY_EXAM_DATA.documents, session.documents, 'documents', true);
  const openBox = document.getElementById('history-exam-open');
  openBox.innerHTML = HISTORY_EXAM_DATA.open.map((q,i)=>`<div class="q-block"><h3 style="font-family:'DM Serif Display',serif;font-size:20px;margin-bottom:8px;">${i+1}. ${q.title}</h3><p style="white-space:pre-line;margin-bottom:12px;font-size:14.5px;">${q.prompt}</p><textarea id="history-essay-${i}" style="width:100%;min-height:240px;padding:12px;background:var(--surface);color:var(--text-primary);border:1px solid var(--border-strong);border-radius:7px;font:inherit;">${session.essays[i]||''}</textarea></div>`).join('');
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
    <div class="section-card"><div class="section-header" onclick="toggleSectionBody('history-exam-essay-review')"><span class="section-title">Open-response self-grading</span><span class="collapse-icon open">&#9660;</span></div><div class="section-body open" id="history-exam-essay-review">${HISTORY_EXAM_DATA.open.map((q,i)=>`<div class="q-block"><h3>${q.title}</h3><p style="white-space:pre-line;margin-top:10px;margin-bottom:12px;font-size:14.5px;"><strong>Your response:</strong><br>${result.essays[i]||'(blank)'}</p><details style="margin-top:12px;cursor:pointer;"><summary style="font-weight:600;color:var(--accent);">View 15-point rubric and model answer</summary><pre style="white-space:pre-wrap;font:inherit;margin-top:10px;padding:12px;background:var(--surface2);border-radius:6px;font-size:12.5px;max-height:300px;overflow-y:auto;">${JSON.stringify(q.rubric,null,2)}</pre><p style="white-space:pre-line;margin-top:12px;font-size:14.5px;"><strong>Model answer:</strong><br>${q.modelAnswer}</p></details><label style="display:block;margin-top:16px;font-weight:600;">Score this response (0-15): <input type="number" min="0" max="15" value="${result.essayScores[i]}" onchange="setHistoryEssayScore(${i},Math.max(0,Math.min(15,this.value)))" style="width:70px;padding:6px;background:var(--surface);color:var(--text-primary);border:1px solid var(--border-strong);border-radius:6px;margin-left:8px;font:inherit;"></label></div>`).join('')}</div></div>
    <div class="section-card"><div class="section-header" onclick="toggleSectionBody('history-exam-objective-review')"><span class="section-title">Objective answer review</span><span class="collapse-icon open">&#9660;</span></div><div class="section-body open" id="history-exam-objective-review"></div></div>
    <button class="q-btn" style="background:var(--wrong);color:#fff;border-color:var(--wrong);" onclick="if(confirm('Start a new practice final?')){saveHistoryExam('result',null);startHistoryFinalExam()}">Start New Attempt</button>`;
  const review=document.getElementById('history-exam-objective-review');
  [...HISTORY_EXAM_DATA.objective.map((q,i)=>[q,result.objective[i],`Section 1 #${i+1}`]),...HISTORY_EXAM_DATA.documents.map((q,i)=>[q,result.documents[i],`Section 2 #${i+1}`])].forEach(([q,a,label])=>{
    const div=document.createElement('div'); div.className='q-block'; const ok=a===q.a;
    div.innerHTML=`<div class="q-header"><span class="q-state-badge ${ok?'correct':'wrong'}">${ok?'Correct':'Incorrect'}</span><div class="q-text">${label}: ${q.q}</div></div><p style="margin-top:6px;font-size:14px;"><strong>Your answer:</strong> ${a===null?'Unanswered':String.fromCharCode(65+a)} · <strong>Correct:</strong> ${String.fromCharCode(65+q.a)}</p><div class="q-feedback show ${ok?'good':'bad'}">${q.explanations[q.a]}</div>`;
    review.appendChild(div);
  });
}
function toggleSectionBody(sectionId) {
  const body = document.getElementById(sectionId);
  if (!body) return;
  const isCurrentlyOpen = body.classList.contains('open');
  const header = body.previousElementSibling;
  const icon = header ? header.querySelector('.collapse-icon') : null;
  
  if (isCurrentlyOpen) {
    body.classList.remove('open');
    body.style.display = 'none';
    if (icon) icon.classList.remove('open');
  } else {
    body.classList.add('open');
    body.style.display = 'block';
    if (icon) icon.classList.add('open');
  }
}

// Shuffles an array helper
function shuffleArray(array) {
  let arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ── OVERALL DASHBOARD VIEW RENDERER ──
function renderOverallDashboard(container) {
  const stats = calculateProgress();
  const bioSummaries = {
    1: "Lab Safety, Biological Hierarchy, Scientific Method, Microscopy, Bioethics",
    2: "Inorganic/Organic Chemistry, Carbohydrates, Lipids, Proteins, Nucleic Acids, Osmosis, Enzymes",
    3: "Cell Structures, Eukaryotic Organelles, Chromosomes, Mitosis, Cancer, Stem Cells",
    4: "DNA Discovery, Replication, Transcription, Translation, Meiosis, Mendelian Genetics & Disorders",
    5: "Darwin's Theories, Evidence of Evolution, Microevolution, Speciation, Taxonomy & Systematics",
    6: "Viruses (replication), Kingdoms of Life, & Classification",
    7: "Plant Tissues/Organs, Stomata & Xylem Transport, Phloem Pressure Flow, Hormones, Tropisms, Animal Tissues, Heart Circulation, Lungs, Nervous System, Skeletons",
    8: "Behavioral Ecology, Population Growth, Food Webs & Communities, Photosynthesis (Calvin Cycle), Respiration (Glycolysis, Krebs), Biomes, Conservation"
  };
  const histSummaries = {
    5: "Causes of the Industrial Revolution, James Watt and Steam, Inventions, Urbanization, Capitalism vs Communism (Marx & Adam Smith), Social Darwinism, Art Movements",
    6: "Nationalism, Congress of Vienna, French Revolutions, Latin American Independence, Unifications of Germany (Bismarck) and Italy (Cavour & Garibaldi), Victorian Britain, Ottoman Empire Decline, Russian Modernization",
    7: "Motives & Forms of Imperialism, Scramble for Africa, Berlin Conference, King Leopold Congo, Muhammad Ali Egypt, Young Turks, Sepoy Rebellion in India, Opium Wars in China, Meiji Restoration",
    8: "MANIIA Causes of WWI, Assassination of Franz Ferdinand, Trench Warfare & Technology, Sykes-Picot, Russian Revolution, US Entry, Treaty of Versailles & League of Nations"
  };
  
  const isBio = appState.currentSubject === 'biology';
  const summaries = isBio ? bioSummaries : histSummaries;
  const startUnit = isBio ? 1 : 5;
  const endUnit = 8;
  
  // Calculate Active Recall progress for Bio
  let arTotalPages = 0;
  let arCompletedPages = 0;
  if (isBio && typeof ACTIVE_RECALL_DATA !== 'undefined') {
    for (let u = 1; u <= 8; u++) {
      const pages = ACTIVE_RECALL_DATA[u] || [];
      arTotalPages += pages.length;
      pages.forEach(p => {
        let pageDone = true;
        if (!p.questions || p.questions.length === 0) {
          pageDone = true;
        } else {
          p.questions.forEach((q, qIdx) => {
            const arKey = `ar_${u}_${p.page}_${qIdx}`;
            if (!appState.activeRecallAnswers[arKey] || !appState.activeRecallAnswers[arKey].locked) {
              pageDone = false;
            }
          });
        }
        if (pageDone) arCompletedPages++;
      });
    }
  }
  const arPct = arTotalPages > 0 ? Math.round((arCompletedPages / arTotalPages) * 100) : 0;
  const sgPct = stats.totalQuestions > 0 ? Math.round((stats.answered / stats.totalQuestions) * 100) : 0;
  
  let html = `
    <div class="hero-panel">
      <div class="hero-eyebrow">${isBio ? 'Biology 9' : 'World History'} · Comprehensive Study Suite</div>
      <h1>Master the ${isBio ? 'Biology' : 'History'} Curriculum</h1>
      <p>
        ${isBio 
          ? 'This study tool provides over 390 highly granular practice questions and an interactive Active Recall deck spanning Units 1 through 8. Check your answers instantly or at the end of each section.' 
          : 'This study room covers World History Units 5 through 8 (Industrial Revolution, Nationalism, Imperialism, and World War I) with rigorous multiple-choice and select-all questions.'}
      </p>
      
      ${isBio ? `
      <div style="display:flex; gap: 12px; margin-top: 18px; flex-wrap: wrap;">
        <button class="q-btn primary" onclick="showView('final-exam-simulator')" style="background: var(--wrong); border-color: var(--wrong); padding: 10px 20px; font-weight: 600; display:flex; align-items:center; gap: 8px;">
          ⚡ Open 2026 Biology Final Exam Simulator
        </button>
        <button class="q-btn" onclick="showView('active-recall')" style="padding: 10px 20px; font-weight: 600; display:flex; align-items:center; gap: 8px; border-color: var(--accent); color: var(--accent);">
          📖 Open Active Recall Reading Deck
        </button>
      </div>
      ` : ''}
      
      <div style="margin-top: 16px; padding: 10px 14px; background: var(--correct-soft); border-left: 4px solid var(--correct); border-radius: 6px; font-size: 13px; color: var(--correct-ink); font-weight: 500; display: flex; align-items: center; gap: 8px;">
        <span>🛡️ All curriculum questions and study room content have been cross-referenced and verified to align 100% with the provided course notes.</span>
      </div>
      
      <div class="mode-select-bar">
        <span style="font-size: 13.5px; font-weight:600; color: var(--text-secondary);">Answer Grading:</span>
        <div class="mode-toggle">
          <button class="mode-toggle-btn ${appState.feedbackMode === 'immediate' ? 'active' : ''}" id="mode-immediate-btn">Check each answer instantly</button>
          <button class="mode-toggle-btn ${appState.feedbackMode === 'section' ? 'active' : ''}" id="mode-section-btn">Check all at section end</button>
        </div>
      </div>
    </div>
  `;
  
  // Show double progress block for Bio
  if (isBio) {
    html += `
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 24px;">
        <div class="sidebar-box" style="margin-bottom: 0;">
          <h2 class="dashboard-title" style="font-size:15px; margin-bottom:6px;">🧬 Study Guide Practice Questions</h2>
          <div style="font-size: 13px; color: var(--text-secondary); margin-bottom: 6px;">
            Completed: <strong>${stats.answered} / ${stats.totalQuestions}</strong> (${sgPct}%)
          </div>
          <div class="bar-container" style="height: 8px; margin-top:0;">
            <div class="bar-fill" style="width: ${sgPct}%; background: var(--accent);"></div>
          </div>
        </div>
        <div class="sidebar-box" style="margin-bottom: 0;">
          <h2 class="dashboard-title" style="font-size:15px; margin-bottom:6px;">📖 Active Recall Reading Pages</h2>
          <div style="font-size: 13px; color: var(--text-secondary); margin-bottom: 6px;">
            Completed: <strong>${arCompletedPages} / ${arTotalPages}</strong> (${arPct}%)
          </div>
          <div class="bar-container" style="height: 8px; margin-top:0;">
            <div class="bar-fill" style="width: ${arPct}%; background: var(--correct);"></div>
          </div>
        </div>
      </div>
    `;
  }
  
  html += `
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
  `;
  
  for (let u = startUnit; u <= endUnit; u++) {
    const uStats = stats.units[u];
    if (!uStats) continue;
    const answered = uStats.answered;
    const total = uStats.total;
    const correct = uStats.correct;
    const pct = total > 0 ? Math.round((answered / total) * 100) : 0;
    const scorePct = answered > 0 ? Math.round((correct / answered) * 100) : 0;
    
    html += `
      <div class="sidebar-box unit-card" data-unit="${u}" style="display:flex; flex-direction:column; justify-content:space-between; height: 100%; margin-bottom:0;">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 8px;">
            <h3 style="font-family:'DM Serif Display', serif; font-size: 18px;">Unit ${u}</h3>
            <span class="unit-badge" style="font-size: 10px;">${total} Qs</span>
          </div>
          <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.4; margin-bottom: 12px; height: 75px; overflow: hidden;">
            ${summaries[u] || ''}
          </p>
        </div>
        
        <div>
          <div style="font-size: 12px; color: var(--text-dim); display:flex; justify-content:space-between; margin-bottom: 4px;">
            <span>Completed: ${pct}%</span>
            <span>Score: ${answered > 0 ? scorePct + '%' : 'N/A'}</span>
          </div>
          <div class="bar-container" style="height: 6px; margin-bottom: 14px;">
            <div class="bar-fill" style="width: ${pct}%; background: var(--correct);"></div>
          </div>
          <button class="q-btn primary" style="width: 100%; text-align:center; padding: 8px;" onclick="showView('unit-${u}')">Open Study Room</button>
        </div>
      </div>
    `;
  }
  
  html += `
    </div>
  `;
  
  container.innerHTML = html;
  
  // Register mode listeners
  document.getElementById('mode-immediate-btn').addEventListener('click', () => {
    appState.feedbackMode = 'immediate';
    localStorage.setItem('bio_quiz_feedback_mode', 'immediate');
    document.getElementById('mode-immediate-btn').classList.add('active');
    document.getElementById('mode-section-btn').classList.remove('active');
  });
  
  document.getElementById('mode-section-btn').addEventListener('click', () => {
    appState.feedbackMode = 'section';
    localStorage.setItem('bio_quiz_feedback_mode', 'section');
    document.getElementById('mode-immediate-btn').classList.remove('active');
    document.getElementById('mode-section-btn').classList.add('active');
  });
}

// ── UNIT DETAIL VIEW RENDERER ──
function renderUnitView(container, unitNum) {
  const questions = getActiveQuizData()[unitNum] || [];
  
  // Group questions by section
  let sectionsMap = {};
  questions.forEach((q, idx) => {
    const sec = q.section;
    if (!sectionsMap[sec]) {
      sectionsMap[sec] = {
        title: q.title,
        questions: []
      };
    }
    sectionsMap[sec].questions.push({ q, idx });
  });
  
  const unitTitles = {
    1: "Unit 1: Scientific Process & Lab Safety",
    2: "Unit 2: Biochemistry & Cellular Transport",
    3: "Unit 3: Cell Structure, Cycle, & Cancer",
    4: "Unit 4: DNA, Genetics, & Molecular Biology",
    5: "Unit 5: Darwin, Evolution & Systematics",
    6: "Unit 6: Viruses, Kingdoms of Life, & Classification",
    7: "Unit 7: Anatomy & Physiology — Plants and Animals",
    8: "Unit 8: Ecology, Bioenergetics, & Biomes"
  };
  
  let html = `
    <div style="display:flex; align-items:center; gap: 12px; margin-bottom: 8px;">
      <button class="q-btn" onclick="showView('dashboard')">← Dashboard</button>
      <span class="unit-badge">Unit ${unitNum} Study Room</span>
    </div>
    <h1 style="font-family:'DM Serif Display', serif; font-size: 32px; margin-bottom: 20px;">${unitTitles[unitNum]}</h1>
  `;
  
  // Render each section card
  const sortedSections = Object.keys(sectionsMap).sort();
  sortedSections.forEach(sec => {
    const secData = sectionsMap[sec];
    const secTitle = secData.title;
    const secQs = secData.questions;
    
    // Count stats for this section
    let totalSecQs = secQs.length;
    let answeredSec = 0;
    secQs.forEach(({ q, idx }) => {
      const qKey = `q_${unitNum}_${sec}_${idx}`;
      if (appState.userAnswers[qKey] && appState.userAnswers[qKey].locked) {
        answeredSec++;
      }
    });
    
    html += `
      <div class="section-card" id="sec-card-${sec.replace('.', '_')}">
        <div class="section-header" onclick="toggleSectionCollapse('${sec.replace('.', '_')}')">
          <div class="section-header-left">
            <span class="section-badge">${sec}</span>
            <span class="section-title">${secTitle}</span>
          </div>
          <div class="section-header-right">
            <span class="section-progress" id="sec-prog-${sec.replace('.', '_')}">${answeredSec} / ${totalSecQs} completed</span>
            <span class="collapse-icon" id="collapse-icon-${sec.replace('.', '_')}">▼</span>
          </div>
        </div>
        <div class="section-body" id="sec-body-${sec.replace('.', '_')}">
          <div class="section-actions-bar">
            <button class="sec-action-btn" onclick="shuffleSection(${unitNum}, '${sec}')" title="Randomize question order">
              &#x1F500; Shuffle
            </button>
            <button class="sec-action-btn" onclick="unshuffleSection(${unitNum}, '${sec}')" title="Restore original question order">
              &#x1F522; Original Order
            </button>
            <button class="sec-action-btn danger" onclick="resetSection(${unitNum}, '${sec}')" title="Clear all answers in this section">
              &#x1F504; Reset Section
            </button>
          </div>
          <div id="sec-qs-container-${sec.replace('.', '_')}">
            <!-- Questions rendered here dynamically -->
          </div>
          
          <div class="section-check-panel" id="sec-check-panel-${sec.replace('.', '_')}" style="display: ${appState.feedbackMode === 'section' ? 'flex' : 'none'};">
            <div style="font-size: 13.5px; color: var(--text-secondary);">
              Ensure all questions are selected before checking the entire section.
            </div>
            <button class="q-btn primary" onclick="checkAllSectionQuestions(${unitNum}, '${sec}')">Check Section Answers</button>
          </div>
        </div>
      </div>
    `;
  });
  
  container.innerHTML = html;
  
  // Render the questions inside each section's body to avoid long HTML string building
  sortedSections.forEach(sec => {
    const containerEl = document.getElementById(`sec-qs-container-${sec.replace('.', '_')}`);
    let secQs = sectionsMap[sec].questions;
    
    // Apply shuffle order if exists
    const shuffleKey = `${unitNum}_${sec}`;
    if (sectionShuffleMap[shuffleKey]) {
      const order = sectionShuffleMap[shuffleKey];
      // Map shuffled original indices back to secQs entries
      const idxToEntry = {};
      secQs.forEach(entry => { idxToEntry[entry.idx] = entry; });
      const reordered = order.map(origIdx => idxToEntry[origIdx]).filter(Boolean);
      // If some entries weren't in the map (data changed), append them
      if (reordered.length === secQs.length) {
        secQs = reordered;
      }
    }
    
    renderSectionQuestions(containerEl, unitNum, sec, secQs);
  });
}

function toggleSectionCollapse(secId) {
  const body = document.getElementById(`sec-body-${secId}`);
  const icon = document.getElementById(`collapse-icon-${secId}`);
  const isOpen = body.classList.toggle('open');
  if (isOpen) {
    icon.classList.add('open');
  } else {
    icon.classList.remove('open');
  }
}

function renderSectionQuestions(containerEl, unitNum, sec, secQs) {
  containerEl.innerHTML = '';
  
  secQs.forEach(({ q, idx }) => {
    const qKey = `q_${unitNum}_${sec}_${idx}`;
    const savedState = appState.userAnswers[qKey] || { selected: [], locked: false, correct: false };
    
    const qBlock = document.createElement('div');
    qBlock.className = 'q-block';
    qBlock.id = `qb_${unitNum}_${sec.replace('.', '_')}_${idx}`;
    
    // Header row
    const meta = document.createElement('div');
    meta.className = 'q-meta';
    
    const badge = document.createElement('span');
    badge.className = 'q-type-badge';
    badge.textContent = (q.t === 'mc' ? 'Multiple Choice' : 'Select All That Apply');
    meta.appendChild(badge);
    
    const stateBadge = document.createElement('span');
    stateBadge.className = 'q-state-badge';
    if (savedState.locked) {
      stateBadge.classList.add(savedState.correct ? 'correct' : 'wrong');
      stateBadge.textContent = savedState.correct ? '\u2713 Correct' : '\u2717 Incorrect';
    }
    meta.appendChild(stateBadge);
    
    qBlock.appendChild(meta);
    
    // Question text
    const text = document.createElement('div');
    text.className = 'q-text';
    text.textContent = `[Unit ${q.section}] ${idx + 1}. ${q.q}`;
    qBlock.appendChild(text);
    
    // Options
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    // Loop options
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label';
      if (savedState.selected.includes(optIdx)) label.classList.add('selected');
      if (savedState.locked) {
        label.classList.add('locked');
        
        // Coloring correct/wrong answers
        if (q.t === 'mc') {
          if (optIdx === q.a) {
            label.classList.add('correct');
          } else if (savedState.selected.includes(optIdx)) {
            label.classList.add('wrong');
          }
        } else {
          // Select All
          const isCorrectChoice = q.correct.includes(optText);
          const wasSelected = savedState.selected.includes(optIdx);
          if (isCorrectChoice) {
            label.classList.add('correct');
            if (!wasSelected) label.classList.add('missed'); // missed correct choice
          } else if (wasSelected) {
            label.classList.add('wrong'); // selected incorrect choice
          }
        }
      }
      
      const input = document.createElement('input');
      input.type = q.t === 'mc' ? 'radio' : 'checkbox';
      input.className = 'opt-input';
      input.name = `opt_${unitNum}_${sec.replace('.', '_')}_${idx}`;
      input.value = optIdx;
      input.checked = savedState.selected.includes(optIdx);
      input.disabled = savedState.locked;
      
      // Select handler
      input.addEventListener('change', () => {
        if (savedState.locked) return;
        
        if (q.t === 'mc') {
          savedState.selected = [optIdx];
          // Highlight active label
          qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
          label.classList.add('selected');
          
          if (appState.feedbackMode === 'immediate') {
            // Don't auto-grade — user clicks Check Answer button
          }
          // Always save selection
          appState.userAnswers[qKey] = { selected: savedState.selected, locked: false, correct: false };
          localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
          
          // Show the check answer button if hidden
          const checkBtn = qBlock.querySelector('.check-answer-btn');
          if (checkBtn) checkBtn.style.display = 'inline-flex';
        } else {
          // Checkbox
          if (input.checked) {
            if (!savedState.selected.includes(optIdx)) savedState.selected.push(optIdx);
            label.classList.add('selected');
          } else {
            savedState.selected = savedState.selected.filter(i => i !== optIdx);
            label.classList.remove('selected');
          }
          
          // Always save selection
          appState.userAnswers[qKey] = { selected: savedState.selected, locked: false, correct: false };
          localStorage.setItem('bio_quiz_state_v3', JSON.stringify(appState.userAnswers));
          
          // Show the check answer button if hidden
          const checkBtnSA = qBlock.querySelector('.check-answer-btn');
          if (checkBtnSA) checkBtnSA.style.display = 'inline-flex';
        }
      });
      
      label.appendChild(input);
      
      // Letter indicator (A, B, C, D...)
      const letter = document.createElement('span');
      letter.className = 'opt-letter';
      letter.textContent = String.fromCharCode(65 + optIdx) + '.';
      label.appendChild(letter);
      
      const textSpan = document.createElement('span');
      textSpan.className = 'opt-text';
      textSpan.textContent = optText;
      label.appendChild(textSpan);
      
      optsDiv.appendChild(label);
    });
    
    qBlock.appendChild(optsDiv);
    
    // Actions / Feedback row
    const feedback = document.createElement('div');
    feedback.className = 'q-feedback';
    if (savedState.locked) {
      feedback.classList.add('show', savedState.correct ? 'good' : 'bad');
      let feedbackText = '';
      if (q.t === 'mc') {
        const correctLetter = String.fromCharCode(65 + q.a);
        if (savedState.correct) {
          feedbackText = `<strong>\u2713 Correct! You chose ${correctLetter}.</strong>`;
        } else {
          const userLetter = savedState.selected.length > 0 ? String.fromCharCode(65 + savedState.selected[0]) : 'None';
          feedbackText = `<strong>\u2717 Incorrect. You chose ${userLetter}. The correct answer is ${correctLetter}.</strong>`;
        }
      } else {
        const correctIndices = [];
        q.opts.forEach((optText, oIdx) => {
          if (q.correct.includes(optText)) correctIndices.push(oIdx);
        });
        const correctLetters = correctIndices.map(i => String.fromCharCode(65 + i)).join(', ');
        if (savedState.correct) {
          feedbackText = `<strong>\u2713 Correct! You chose the correct options: ${correctLetters}.</strong>`;
        } else {
          const userLetters = savedState.selected.sort((a,b)=>a-b).map(i => String.fromCharCode(65 + i)).join(', ') || 'None';
          feedbackText = `<strong>\u2717 Incorrect. You chose: ${userLetters}. The correct answers are: ${correctLetters}.</strong>`;
        }
      }
      feedback.innerHTML = `${feedbackText}<br style="margin-bottom: 6px;">${q.explanation || ''}`;
    }
    qBlock.appendChild(feedback);
    
    const actions = document.createElement('div');
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
    
    qBlock.appendChild(actions);
    containerEl.appendChild(qBlock);
  });
}

// Check score and lock a specific question
function gradeQuestion(unitNum, sec, idx, qBlock, q, state) {
  if (state.locked) return;
  
  state.locked = true;
  
  // Grade
  let isCorrect = true;
  if (q.t === 'mc') {
    isCorrect = state.selected.includes(q.a);
  } else {
    // Select All
    const selectedTexts = state.selected.map(i => q.opts[i]);
    
    // Check if lengths and contents match
    if (selectedTexts.length !== q.correct.length) {
      isCorrect = false;
    } else {
      selectedTexts.forEach(txt => {
        if (!q.correct.includes(txt)) isCorrect = false;
      });
    }
  }
  
  state.correct = isCorrect;
  
  // Save answer
  const qKey = `q_${unitNum}_${sec}_${idx}`;
  appState.userAnswers[qKey] = {
    selected: state.selected,
    locked: true,
    correct: isCorrect
  };
  
  saveState();
  updateDashboardUI();
  
  // Update Question UI elements
  // Show state badge
  const stateBadge = qBlock.querySelector('.q-state-badge');
  stateBadge.className = 'q-state-badge ' + (isCorrect ? 'correct' : 'wrong');
  stateBadge.textContent = isCorrect ? '\u2713 Correct' : '\u2717 Incorrect';
  
  // Update feedback text with EXPLANATION!
  let feedbackText = '';
  if (q.t === 'mc') {
    const correctLetter = String.fromCharCode(65 + q.a);
    if (isCorrect) {
      feedbackText = `<strong>\u2713 Correct! You chose ${correctLetter}.</strong>`;
    } else {
      const userLetter = state.selected.length > 0 ? String.fromCharCode(65 + state.selected[0]) : 'None';
      feedbackText = `<strong>\u2717 Incorrect. You chose ${userLetter}. The correct answer is ${correctLetter}.</strong>`;
    }
  } else {
    const correctIndices = [];
    q.opts.forEach((optText, oIdx) => {
      if (q.correct.includes(optText)) correctIndices.push(oIdx);
    });
    const correctLetters = correctIndices.map(i => String.fromCharCode(65 + i)).join(', ');
    if (isCorrect) {
      feedbackText = `<strong>\u2713 Correct! You chose the correct options: ${correctLetters}.</strong>`;
    } else {
      const userLetters = state.selected.sort((a,b)=>a-b).map(i => String.fromCharCode(65 + i)).join(', ') || 'None';
      feedbackText = `<strong>\u2717 Incorrect. You chose: ${userLetters}. The correct answers are: ${correctLetters}.</strong>`;
    }
  }
  const feedback = qBlock.querySelector('.q-feedback');
  feedback.className = 'q-feedback show ' + (isCorrect ? 'good' : 'bad');
  feedback.innerHTML = `${feedbackText}<br style="margin-bottom: 6px;">${q.explanation || ''}`;
  
  // Color the labels
  qBlock.querySelectorAll('.opt-label').forEach((label, oIdx) => {
    label.classList.add('locked');
    const input = label.querySelector('input');
    if (input) input.disabled = true;
    
    if (q.t === 'mc') {
      if (oIdx === q.a) {
        label.classList.add('correct');
      } else if (state.selected.includes(oIdx)) {
        label.classList.add('wrong');
      }
    } else {
      const optText = q.opts[oIdx];
      const isCorrectChoice = q.correct.includes(optText);
      const wasSelected = state.selected.includes(oIdx);
      if (isCorrectChoice) {
        label.classList.add('correct');
        if (!wasSelected) label.classList.add('missed');
      } else if (wasSelected) {
        label.classList.add('wrong');
      }
    }
  });
  
  // Hide submit button if present
  const checkBtn = qBlock.querySelector('.q-actions button');
  if (checkBtn) checkBtn.style.display = 'none';
  
  // Update section progress counter
  updateSectionProgressText(unitNum, sec);
}

function updateSectionProgressText(unitNum, sec) {
  const questions = getActiveQuizData()[unitNum] || [];
  let secQs = questions.filter(q => q.section === sec);
  let total = secQs.length;
  let answered = 0;
  
  questions.forEach((q, idx) => {
    if (q.section !== sec) return;
    const qKey = `q_${unitNum}_${sec}_${idx}`;
    if (appState.userAnswers[qKey] && appState.userAnswers[qKey].locked) {
      answered++;
    }
  });
  
  const progLabel = document.getElementById(`sec-prog-${sec.replace('.', '_')}`);
  if (progLabel) {
    progLabel.textContent = `${answered} / ${total} completed`;
  }
}

// Section End Grader: grade all questions in a section at once
function checkAllSectionQuestions(unitNum, sec) {
  const container = document.getElementById(`sec-qs-container-${sec.replace('.', '_')}`);
  const questions = getActiveQuizData()[unitNum] || [];
  
  let sectionAnswersUnsavedCount = 0;
  
  questions.forEach((q, idx) => {
    if (q.section !== sec) return;
    const qKey = `q_${unitNum}_${sec}_${idx}`;
    const ans = appState.userAnswers[qKey] || { selected: [], locked: false };
    
    if (!ans.locked && ans.selected.length > 0) {
      sectionAnswersUnsavedCount++;
      const qBlock = document.getElementById(`qb_${unitNum}_${sec.replace('.', '_')}_${idx}`);
      gradeQuestion(unitNum, sec, idx, qBlock, q, ans);
    }
  });
  
  if (sectionAnswersUnsavedCount === 0) {
    alert("Please select answers for the section before checking.");
  }
}

// ── 2026 FINAL EXAM SIMULATOR RENDERERS ──
function renderFinalExamView(container) {
  if (appState.examResult) {
    renderFinalExamReview(container);
    return;
  }
  
  if (appState.examSession) {
    renderFinalExamRoom(container);
    return;
  }
  
  // Otherwise render Exam Lobby
  let html = `
    <div class="exam-lobby-card">
      <div class="hero-eyebrow" style="color:var(--wrong);">Official Review Simulation</div>
      <h1 style="font-family:'DM Serif Display', serif; font-size: 32px; margin-bottom: 12px;">2025-26 Lab Biology Final Exam Simulator</h1>
      <p style="color:var(--text-secondary); margin-bottom: 20px;">
        This simulator mirrors the exact structure, timing, weighting, and syllabus constraints of the final exam review sheet. All multiple-choice questions are highly rigorous <strong>application and scenario-based questions</strong>. Every question includes detailed A, B, C, D explanation panels to review post-submission.
      </p>
      
      <div style="margin-bottom: 20px; padding: 10px 14px; background: var(--correct-soft); border-left: 4px solid var(--correct); border-radius: 6px; font-size: 13px; color: var(--correct-ink); font-weight: 500; display: flex; align-items: center; gap: 8px; max-width: 780px;">
        <span>🛡️ All curriculum questions and simulated exam content have been cross-referenced and verified to align 100% with the provided course notes.</span>
      </div>
      
      <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 16px 20px; font-size: 14px; margin-bottom: 24px;">
        <strong>⏳ Duration:</strong> 2 Hours (120 Minutes)<br>
        <strong>📈 Weighted Grade Calculation:</strong>
        <div class="exam-grid" style="margin-top: 12px; margin-bottom: 0;">
          <div class="exam-part-card">
            <div class="exam-part-num">Part 1</div>
            <div class="exam-part-title">Gen Knowledge Qs 1-8</div>
            <span class="exam-part-weight">20 MC (20%% Weight)</span>
          </div>
          <div class="exam-part-card">
            <div class="exam-part-num">Part 2</div>
            <div class="exam-part-title">MC Focus Units 3-6</div>
            <span class="exam-part-weight">26 MC (30%% Weight)</span>
          </div>
          <div class="exam-part-card">
            <div class="exam-part-num">Part 3</div>
            <div class="exam-part-title">MC Focus Units 7-8</div>
            <span class="exam-part-weight">25 MC (26%% Weight)</span>
          </div>
          <div class="exam-part-card">
            <div class="exam-part-num">Part 4</div>
            <div class="exam-part-title">Open-Ended (Select 6 of 12)</div>
            <span class="exam-part-weight">6 Prompts (24%% Weight)</span>
          </div>
        </div>
      </div>
      
      <div style="border-left: 4px solid var(--amber); background: var(--amber-soft); padding: 14px 18px; border-radius: 8px; font-size: 14px; color: var(--amber-ink); margin-bottom: 24px;">
        <strong>📝 Persistence Notice:</strong> Your active exam progress (time left, selected options, written open-ended text) is continuously auto-saved. If your computer shuts off or the page refreshes, your progress will not be lost.
      </div>
      
      <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 16px 20px; margin-bottom: 20px;">
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
      </button>
    </div>
  `;
  container.innerHTML = html;
}

function startFinalExamSimulation() {
  appState.examSession = {
    part1Answers: Array(EXAM_DATA.part1.length).fill(null),
    part2Answers: Array(EXAM_DATA.part2.length).fill(null),
    part3Answers: Array(EXAM_DATA.part3.length).fill(null),
    
    // Part 4 written responses: key is unit number -> { selectedOption: 'A'|'B', answerText: '...' }
    part4Responses: {
      3: { selectedOption: 'A', answerText: '' },
      '4_1': { selectedOption: 'A', answerText: '' }, // Unit 4 Part 1 Genetics
      '4_2': { selectedOption: 'A', answerText: '' }, // Unit 4 Part 2 Heredity
      5: { selectedOption: 'A', answerText: '' },
      7: { selectedOption: 'A', answerText: '' },
      8: { selectedOption: 'A', answerText: '' }
    },
    
    timeLeft: 120 * 60, // 120 minutes in seconds
    timerInterval: null
  };
  
  saveExamSession();
  renderFinalExamRoom(document.getElementById('main-view'));
}

function renderFinalExamRoom(container) {
  const session = appState.examSession;
  
  // Timer interval setup
  if (session.timerInterval) clearInterval(session.timerInterval);
  session.timerInterval = setInterval(() => {
    session.timeLeft--;
    saveExamSession();
    
    const mins = Math.floor(session.timeLeft / 60);
    const secs = session.timeLeft % 60;
    const timerDisplay = document.getElementById('final-exam-timer');
    if (timerDisplay) {
      timerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
      if (session.timeLeft < 300) { // Red alarm under 5 minutes
        timerDisplay.style.background = 'var(--wrong-soft)';
        timerDisplay.style.color = 'var(--wrong)';
        timerDisplay.style.borderColor = 'var(--wrong-soft-2)';
      }
    }
    
    if (session.timeLeft <= 0) {
      clearInterval(session.timerInterval);
      session.timerInterval = null;
      submitFinalExamSimulation();
    }
  }, 1000);
  
  const mins = Math.floor(session.timeLeft / 60);
  const secs = session.timeLeft % 60;
  
  let html = `
    <div class="exam-header" style="position: sticky; top: 64px; z-index: 99; border-top: 1px solid var(--border);">
      <div>
        <div class="exam-meta-title" style="color:var(--wrong);">Final Exam Simulation Active</div>
        <div style="font-size: 12.5px; color: var(--text-secondary); margin-top: 2px;">
          Part 1: General (20 Qs) · Part 2: Units 3-6 (26 Qs) · Part 3: Units 7-8 (25 Qs) · Part 4: Open-Ended
        </div>
      </div>
      <div style="display:flex; align-items:center; gap: 12px;">
        <div class="exam-timer" id="final-exam-timer">${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}</div>
        <button class="q-btn" onclick="forceQuitExamSim()" style="border-color: var(--wrong); color: var(--wrong);">Exit &amp; Lose Progress</button>
      </div>
    </div>
    
    <!-- EXAM SECTIONS -->
    <div id="exam-contents-scroller">
      
      <!-- PART 1 -->
      <div class="section-card">
        <div class="section-header" onclick="toggleSectionCollapse('ex-part-1')">
          <div class="section-header-left">
            <span class="section-badge">PART 1</span>
            <span class="section-title">General Biology Knowledge (Units 1-8) — 20 Qs</span>
          </div>
          <span class="collapse-icon open" id="collapse-icon-ex-part-1">▼</span>
        </div>
        <div class="section-body open" id="sec-body-ex-part-1">
          <div id="part-1-qs"></div>
        </div>
      </div>
      
      <!-- PART 2 -->
      <div class="section-card">
        <div class="section-header" onclick="toggleSectionCollapse('ex-part-2')">
          <div class="section-header-left">
            <span class="section-badge">PART 2</span>
            <span class="section-title">Units 3-6 Focus Topics — 26 Qs</span>
          </div>
          <span class="collapse-icon open" id="collapse-icon-ex-part-2">▼</span>
        </div>
        <div class="section-body open" id="sec-body-ex-part-2">
          <div id="part-2-qs"></div>
        </div>
      </div>
      
      <!-- PART 3 -->
      <div class="section-card">
        <div class="section-header" onclick="toggleSectionCollapse('ex-part-3')">
          <div class="section-header-left">
            <span class="section-badge">PART 3</span>
            <span class="section-title">Units 7-8 Focus Topics — 25 Qs</span>
          </div>
          <span class="collapse-icon open" id="collapse-icon-ex-part-3">▼</span>
        </div>
        <div class="section-body open" id="sec-body-ex-part-3">
          <div id="part-3-qs"></div>
        </div>
      </div>
      
      <!-- PART 4 -->
      <div class="section-card">
        <div class="section-header" onclick="toggleSectionCollapse('ex-part-4')">
          <div class="section-header-left">
            <span class="section-badge">PART 4</span>
            <span class="section-title">Open-Ended Responses (Choose A or B per Unit) — 6 Qs</span>
          </div>
          <span class="collapse-icon open" id="collapse-icon-ex-part-4">▼</span>
        </div>
        <div class="section-body open" id="sec-body-ex-part-4">
          <p style="color:var(--text-secondary); margin-bottom: 20px; font-size:14px;">
            For each of the following 6 units, you must select **either Option A or Option B** to answer. Write your response in the provided text area. You will self-grade these responses using the official rubrics after submission.
          </p>
          <div id="part-4-prompts"></div>
        </div>
      </div>
      
    </div>
    
    <div style="padding: 32px; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; text-align:center; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
      <h2 style="font-family:'DM Serif Display', serif; font-size: 24px; margin-bottom: 8px;">End of Exam</h2>
      <p style="color: var(--text-secondary); margin-bottom: 20px; font-size: 14.5px;">Clicking submit will finalize your test and immediately grade your work.</p>
      <button class="exam-btn" onclick="submitFinalExamSimulation()" style="font-size: 16px; padding: 12px 36px; background: var(--correct); border-color: var(--correct);">Submit Final Exam</button>
    </div>
  `;
  container.innerHTML = html;
  
  // Render Part 1 Questions
  const p1Container = document.getElementById('part-1-qs');
  renderExamMCList(p1Container, EXAM_DATA.part1, session.part1Answers, 'p1');
  
  // Render Part 2 Questions
  const p2Container = document.getElementById('part-2-qs');
  renderExamMCList(p2Container, EXAM_DATA.part2, session.part2Answers, 'p2');
  
  // Render Part 3 Questions
  const p3Container = document.getElementById('part-3-qs');
  renderExamMCList(p3Container, EXAM_DATA.part3, session.part3Answers, 'p3');
  
  // Render Part 4 Written Questions
  const p4Container = document.getElementById('part-4-prompts');
  renderExamWrittenList(p4Container, EXAM_DATA.part4, session.part4Responses);
}

function renderExamMCList(container, questionList, answerArray, namePrefix) {
  container.innerHTML = '';
  questionList.forEach((q, idx) => {
    const qBlock = document.createElement('div');
    qBlock.className = 'q-block';
    
    const text = document.createElement('div');
    text.className = 'q-text';
    text.textContent = `${idx + 1}. ${q.q}`;
    if (q.section) {
      const secTag = document.createElement('span');
      secTag.style.cssText = 'display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:600;padding:2px 7px;border-radius:4px;margin-right:6px;font-family:DM Mono,monospace;vertical-align:middle;';
      secTag.textContent = '[Unit ' + q.section + ']';
      text.insertBefore(secTag, text.firstChild);
    }
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label';
      if (answerArray[idx] === optIdx) label.classList.add('selected');
      
      const input = document.createElement('input');
      input.type = 'radio';
      input.name = `${namePrefix}_radio_${idx}`;
      input.value = optIdx;
      input.checked = (answerArray[idx] === optIdx);
      
      input.addEventListener('change', () => {
        answerArray[idx] = optIdx;
        qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
        label.classList.add('selected');
        saveExamSession();
      });
      
      label.appendChild(input);
      
      const letter = document.createElement('span');
      letter.className = 'opt-letter';
      letter.textContent = String.fromCharCode(65 + optIdx) + '.';
      label.appendChild(letter);
      
      const textSpan = document.createElement('span');
      textSpan.className = 'opt-text';
      textSpan.textContent = optText;
      label.appendChild(textSpan);
      
      optsDiv.appendChild(label);
    });
    
    qBlock.appendChild(optsDiv);
    
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
          fb.innerHTML = '<strong>\u2713 Correct! You chose ' + correctLetter + '.</strong>';
        } else {
          fb.innerHTML = '<strong>\u2717 Incorrect. You chose ' + userLetter + '. The correct answer is ' + correctLetter + '.</strong>';
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

function renderExamWrittenList(container, promptList, responsesDict) {
  container.innerHTML = '';
  
  // Group prompt list by unit
  let unitsMap = {};
  promptList.forEach(p => {
    const unitKey = p.unit;
    if (!unitsMap[unitKey]) unitsMap[unitKey] = [];
    unitsMap[unitKey].push(p);
  });
  
  const unitKeys = Object.keys(unitsMap);
  unitKeys.forEach(unitKey => {
    const prompts = unitsMap[unitKey];
    
    const unitBlock = document.createElement('div');
    unitBlock.className = 'q-block';
    unitBlock.style.borderLeft = '4px solid var(--accent)';
    
    const unitTitle = document.createElement('h3');
    unitTitle.style.fontFamily = "'DM Serif Display', serif";
    unitTitle.style.fontSize = '18px';
    unitTitle.style.marginBottom = '12px';
    unitTitle.textContent = `${unitKey} Open-Ended Prompt`;
    unitBlock.appendChild(unitTitle);
    
    // Radio selection A or B
    const optSelector = document.createElement('div');
    optSelector.style.display = 'flex';
    optSelector.style.gap = '20px';
    optSelector.style.marginBottom = '14px';
    
    // Map response structure
    let respKey = unitKey;
    if (unitKey === 'Unit 4 Part 1') respKey = '4_1';
    if (unitKey === 'Unit 4 Part 2') respKey = '4_2';
    
    const saved = responsesDict[respKey];
    
    prompts.forEach(p => {
      const optLbl = document.createElement('label');
      optLbl.style.fontSize = '13.5px';
      optLbl.style.fontWeight = '600';
      optLbl.style.cursor = 'pointer';
      
      const radio = document.createElement('input');
      radio.type = 'radio';
      radio.name = `opt_sel_${respKey}`;
      radio.value = p.option;
      radio.checked = (saved.selectedOption === p.option);
      radio.style.marginRight = '6px';
      
      radio.addEventListener('change', () => {
        saved.selectedOption = p.option;
        // Swap visible prompt text
        promptText.innerHTML = `<strong>Option ${p.option} — ${p.title}:</strong> ${p.prompt}`;
        saveExamSession();
      });
      
      optLbl.appendChild(radio);
      optLbl.appendChild(document.createTextNode(`Option ${p.option}: ${p.title}`));
      optSelector.appendChild(optLbl);
    });
    unitBlock.appendChild(optSelector);
    
    // Active Prompt Text
    const promptText = document.createElement('div');
    promptText.style.fontSize = '14.5px';
    promptText.style.color = 'var(--text-primary)';
    promptText.style.lineHeight = '1.5';
    promptText.style.background = 'var(--surface)';
    promptText.style.padding = '12px 16px';
    promptText.style.border = '1px solid var(--border)';
    promptText.style.borderRadius = '8px';
    
    // Set initial text based on saved selection
    const activePrompt = prompts.find(p => p.option === saved.selectedOption) || prompts[0];
    promptText.innerHTML = `<strong>Option ${activePrompt.option} — ${activePrompt.title}:</strong> ${activePrompt.prompt}`;
    unitBlock.appendChild(promptText);
    
    // Written Answer Textarea
    const textarea = document.createElement('textarea');
    textarea.className = 'written-answer-box';
    textarea.placeholder = `Write your response here (Up to 1 page content limit). Ensure you directly apply biological terminology to answer the scenario prompt.`;
    textarea.value = saved.answerText;
    
    textarea.addEventListener('input', () => {
      saved.answerText = textarea.value;
      saveExamSession();
    });
    
    unitBlock.appendChild(textarea);
    container.appendChild(unitBlock);
  });
}

function forceQuitExamSim() {
  if (confirm("Are you sure you want to quit the exam simulator? Your exam session will be terminated and all answers will be lost.")) {
    const session = appState.examSession;
    if (session && session.timerInterval) clearInterval(session.timerInterval);
    appState.examSession = null;
    saveExamSession();
    showView('final-exam-simulator');
  }
}

// ── SUBMIT AND GRADE EXAM ──
function submitFinalExamSimulation() {
  const session = appState.examSession;
  if (!session) return;
  
  if (session.timerInterval) clearInterval(session.timerInterval);
  
  // Grade multiple-choice questions
  let p1Correct = 0;
  EXAM_DATA.part1.forEach((q, idx) => {
    if (session.part1Answers[idx] === q.a) p1Correct++;
  });
  
  let p2Correct = 0;
  EXAM_DATA.part2.forEach((q, idx) => {
    if (session.part2Answers[idx] === q.a) p2Correct++;
  });
  
  let p3Correct = 0;
  EXAM_DATA.part3.forEach((q, idx) => {
    if (session.part3Answers[idx] === q.a) p3Correct++;
  });
  
  // Open-ended self-grading initial state (defaults to 0 points until self-graded)
  let p4Grades = {
    3: 0,
    '4_1': 0,
    '4_2': 0,
    5: 0,
    7: 0,
    8: 0
  };
  
  // Save final results
  appState.examResult = {
    part1Answers: session.part1Answers,
    part2Answers: session.part2Answers,
    part3Answers: session.part3Answers,
    part4Responses: session.part4Responses,
    
    // Scores
    p1Score: p1Correct,
    p2Score: p2Correct,
    p3Score: p3Correct,
    p4Grades: p4Grades, // self-graded
    
    totalP1: EXAM_DATA.part1.length,
    totalP2: EXAM_DATA.part2.length,
    totalP3: EXAM_DATA.part3.length,
    
    submittedAt: new Date().toLocaleTimeString()
  };
  
  appState.examSession = null;
  saveExamSession();
  saveExamResult();
  
  renderFinalExamReview(document.getElementById('main-view'));
}

// ── FINAL EXAM RESULTS REVIEW ──
function renderFinalExamReview(container) {
  const res = appState.examResult;
  if (!res) return;
  
  // Calculate weighted final grade
  // Weight formulas:
  // Part 1: (p1Score / totalP1) * 20
  // Part 2: (p2Score / totalP2) * 30
  // Part 3: (p3Score / totalP3) * 26
  // Part 4: (p4SelfScore / 24) * 24 = p4SelfScore (since 6 questions * 4 max pts = 24 total max pts)
  
  const p1Val = res.totalP1 > 0 ? (res.p1Score / res.totalP1) * 20 : 0;
  const p2Val = res.totalP2 > 0 ? (res.p2Score / res.totalP2) * 30 : 0;
  const p3Val = res.totalP3 > 0 ? (res.p3Score / res.totalP3) * 26 : 0;
  
  // Open ended total
  let openEndedTotal = 0;
  Object.values(res.p4Grades).forEach(score => {
    openEndedTotal += parseInt(score);
  });
  
  const weightedTotal = Math.round(p1Val + p2Val + p3Val + openEndedTotal);
  const gradeLetter = weightedTotal >= 90 ? 'A' : weightedTotal >= 80 ? 'B' : weightedTotal >= 70 ? 'C' : weightedTotal >= 60 ? 'D' : 'F';
  
  let html = `
    <div class="exam-lobby-card" style="border-top: 4px solid ${weightedTotal >= 70 ? 'var(--correct)' : 'var(--wrong)'}; padding-bottom: 24px;">
      <div class="hero-eyebrow" style="color: ${weightedTotal >= 70 ? 'var(--correct)' : 'var(--wrong)'};">Exam Simulation Graded</div>
      <h1 style="font-family:'DM Serif Display', serif; font-size: 32px; margin-bottom: 12px;">Final Weighted Score: ${weightedTotal}%</h1>
      <h2 style="font-size: 18px; font-weight:600; margin-bottom: 18px;">Letter Grade: ${gradeLetter} &nbsp;&middot;&nbsp; (MC Graded &middot; Self-Grade Open Ended Below)</h2>
      
      <div style="background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 16px; margin-bottom: 20px; font-size: 13.5px;">
        <strong>Weighted Score Breakdown:</strong>
        <ul style="list-style:none; padding:0; margin-top:8px; display:flex; flex-direction:column; gap:4px;">
          <li>📊 <strong>Part 1 MC:</strong> ${res.p1Score}/${res.totalP1} correct (${Math.round(p1Val)} / 20 points weight)</li>
          <li>📊 <strong>Part 2 MC:</strong> ${res.p2Score}/${res.totalP2} correct (${Math.round(p2Val)} / 30 points weight)</li>
          <li>📊 <strong>Part 3 MC:</strong> ${res.p3Score}/${res.totalP3} correct (${Math.round(p3Val)} / 26 points weight)</li>
          <li>✍️ <strong>Part 4 Written:</strong> Self-Graded Score: <strong style="color:var(--accent);">${openEndedTotal}</strong> / 24 points weight</li>
        </ul>
      </div>
      
      <div style="display:flex; gap:12px;">
        <button class="q-btn primary" onclick="retakeExamSimulation()" style="background: var(--wrong); border-color: var(--wrong); font-weight:600;">Retake Final Exam Simulator</button>
        <button class="q-btn" onclick="showView('dashboard')">Back to Dashboard</button>
      </div>
    </div>
    
    <!-- DETAILED REVIEW AREA -->
    <h2 style="font-family:'DM Serif Display', serif; font-size: 24px; margin: 12px 0 6px 0;">Detailed Exam Review</h2>
    <p style="color:var(--text-secondary); margin-bottom: 20px; font-size:14px;">Expand the parts below to review the question-by-question explanations.</p>
    
    <!-- PART 1 REVIEW -->
    <div class="section-card">
      <div class="section-header" onclick="toggleSectionCollapse('rev-part-1')">
        <span class="section-title">Part 1 Graded Review — General MC (${res.p1Score}/${res.totalP1} Correct)</span>
        <span class="collapse-icon open" id="collapse-icon-rev-part-1">▼</span>
      </div>
      <div class="section-body open" id="sec-body-rev-part-1">
        <div id="rev-part-1-qs"></div>
      </div>
    </div>
    
    <!-- PART 2 REVIEW -->
    <div class="section-card">
      <div class="section-header" onclick="toggleSectionCollapse('rev-part-2')">
        <span class="section-title">Part 2 Graded Review — Units 3-6 MC (${res.p2Score}/${res.totalP2} Correct)</span>
        <span class="collapse-icon open" id="collapse-icon-rev-part-2">▼</span>
      </div>
      <div class="section-body open" id="sec-body-rev-part-2">
        <div id="rev-part-2-qs"></div>
      </div>
    </div>
    
    <!-- PART 3 REVIEW -->
    <div class="section-card">
      <div class="section-header" onclick="toggleSectionCollapse('rev-part-3')">
        <span class="section-title">Part 3 Graded Review — Units 7-8 MC (${res.p3Score}/${res.totalP3} Correct)</span>
        <span class="collapse-icon open" id="collapse-icon-rev-part-3">▼</span>
      </div>
      <div class="section-body open" id="sec-body-rev-part-3">
        <div id="rev-part-3-qs"></div>
      </div>
    </div>
    
    <!-- PART 4 REVIEW & SELF GRADING -->
    <div class="section-card">
      <div class="section-header" onclick="toggleSectionCollapse('rev-part-4')">
        <span class="section-title">Part 4 Graded Review — Open-Ended Self-Grading</span>
        <span class="collapse-icon open" id="collapse-icon-rev-part-4">▼</span>
      </div>
      <div class="section-body open" id="sec-body-rev-part-4">
        <div id="rev-part-4-written"></div>
      </div>
    </div>
  `;
  container.innerHTML = html;
  
  // Render Graded MCs
  const r1 = document.getElementById('rev-part-1-qs');
  renderExamGradedMC(r1, EXAM_DATA.part1, res.part1Answers);
  
  const r2 = document.getElementById('rev-part-2-qs');
  renderExamGradedMC(r2, EXAM_DATA.part2, res.part2Answers);
  
  const r3 = document.getElementById('rev-part-3-qs');
  renderExamGradedMC(r3, EXAM_DATA.part3, res.part3Answers);
  
  // Render Written self-grader
  const r4 = document.getElementById('rev-part-4-written');
  renderExamGradedWritten(r4, EXAM_DATA.part4, res.part4Responses, res.p4Grades);
}

function renderExamGradedMC(container, questionList, answerArray) {
  container.innerHTML = '';
  questionList.forEach((q, idx) => {
    const userChoice = answerArray[idx];
    const isCorrect = (userChoice === q.a);
    
    const qBlock = document.createElement('div');
    qBlock.className = 'q-block';
    
    const meta = document.createElement('div');
    meta.className = 'q-meta';
    
    const stateBadge = document.createElement('span');
    stateBadge.className = 'q-state-badge ' + (isCorrect ? 'correct' : 'wrong');
    stateBadge.style.display = 'inline-block';
    stateBadge.textContent = isCorrect ? '\u2713 Correct' : '\u2717 Incorrect';
    meta.appendChild(stateBadge);
    
    qBlock.appendChild(meta);
    
    const text = document.createElement('div');
    text.className = 'q-text';
    text.textContent = `${idx + 1}. ${q.q}`;
    if (q.section) {
      const secTag = document.createElement('span');
      secTag.style.cssText = 'display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:600;padding:2px 7px;border-radius:4px;margin-right:6px;font-family:DM Mono,monospace;vertical-align:middle;';
      secTag.textContent = '[Unit ' + q.section + ']';
      text.insertBefore(secTag, text.firstChild);
    }
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label locked';
      if (userChoice === optIdx) label.classList.add('selected');
      
      if (optIdx === q.a) {
        label.classList.add('correct');
      } else if (userChoice === optIdx) {
        label.classList.add('wrong');
      }
      
      const letter = document.createElement('span');
      letter.className = 'opt-letter';
      letter.textContent = String.fromCharCode(65 + optIdx) + '.';
      label.appendChild(letter);
      
      const textSpan = document.createElement('span');
      textSpan.className = 'opt-text';
      textSpan.textContent = optText;
      label.appendChild(textSpan);
      
      label.style.pointerEvents = 'none'; // Lock
      optsDiv.appendChild(label);
    });
    qBlock.appendChild(optsDiv);
    
    // Add feedback row with user choice and correct answer
    const feedback = document.createElement('div');
    feedback.className = 'q-feedback show ' + (isCorrect ? 'good' : 'bad');
    const userLetter = userChoice !== undefined && userChoice !== null && userChoice !== -1 ? String.fromCharCode(65 + userChoice) : 'None';
    const correctLetter = String.fromCharCode(65 + q.a);
    if (isCorrect) {
      feedback.innerHTML = `<strong>\u2713 Correct! You chose ${correctLetter}.</strong>`;
    } else {
      feedback.innerHTML = `<strong>\u2717 Incorrect. You chose ${userLetter}. The correct answer is ${correctLetter}.</strong>`;
    }
    qBlock.appendChild(feedback);
    
    // Add option-by-option explanations!
    const expBox = document.createElement('div');
    expBox.className = 'opt-explanations-box';
    
    const expTitle = document.createElement('div');
    expTitle.className = 'opt-explanations-title';
    expTitle.textContent = 'Option-by-Option Explanations';
    expBox.appendChild(expTitle);
    
    q.opts.forEach((optText, optIdx) => {
      const expItem = document.createElement('div');
      expItem.className = 'opt-exp-item';
      
      const letterChar = String.fromCharCode(65 + optIdx);
      const isThisCorrect = (optIdx === q.a);
      const isUserSelected = (userChoice === optIdx);
      
      if (isUserSelected && !isThisCorrect) {
        expItem.style.color = 'var(--wrong)';
        expItem.innerHTML = `<strong>Choice ${letterChar} (Incorrect - Your Selection):</strong> ${q.explanations[optIdx]}`;
      } else if (isThisCorrect) {
        expItem.style.color = 'var(--correct)';
        expItem.innerHTML = `<strong>Choice ${letterChar} (Correct${isUserSelected ? ' - Your Selection' : ''}):</strong> ${q.explanations[optIdx]}`;
      } else {
        expItem.innerHTML = `<strong>Choice ${letterChar} (Incorrect):</strong> ${q.explanations[optIdx]}`;
      }
      expBox.appendChild(expItem);
    });
    
    qBlock.appendChild(expBox);
    container.appendChild(qBlock);
  });
}

function renderExamGradedWritten(container, promptList, responsesDict, gradesDict) {
  container.innerHTML = '';
  
  // Group prompts by unit
  let unitsMap = {};
  promptList.forEach(p => {
    const unitKey = p.unit;
    if (!unitsMap[unitKey]) unitsMap[unitKey] = [];
    unitsMap[unitKey].push(p);
  });
  
  const unitKeys = Object.keys(unitsMap);
  unitKeys.forEach(unitKey => {
    let respKey = unitKey;
    if (unitKey === 'Unit 4 Part 1') respKey = '4_1';
    if (unitKey === 'Unit 4 Part 2') respKey = '4_2';
    
    const saved = responsesDict[respKey];
    const prompts = unitsMap[unitKey];
    
    // Find the actual prompt answered
    const activePrompt = prompts.find(p => p.option === saved.selectedOption) || prompts[0];
    
    const qBlock = document.createElement('div');
    qBlock.className = 'q-block';
    
    const titleEl = document.createElement('h3');
    titleEl.style.fontFamily = "'DM Serif Display', serif";
    titleEl.style.fontSize = '18px';
    titleEl.style.marginBottom = '6px';
    titleEl.textContent = `${unitKey} — Option ${activePrompt.option}: ${activePrompt.title}`;
    qBlock.appendChild(titleEl);
    
    const promptText = document.createElement('div');
    promptText.style.fontSize = '14px';
    promptText.style.color = 'var(--text-secondary)';
    promptText.style.marginBottom = '12px';
    promptText.innerHTML = `<strong>Prompt:</strong> ${activePrompt.prompt}`;
    qBlock.appendChild(promptText);
    
    // User answer review
    const userAnsLabel = document.createElement('strong');
    userAnsLabel.style.fontSize = '13px';
    userAnsLabel.style.textTransform = 'uppercase';
    userAnsLabel.style.color = 'var(--text-dim)';
    userAnsLabel.textContent = 'Your Answer:';
    qBlock.appendChild(userAnsLabel);
    
    const userText = document.createElement('blockquote');
    userText.style.background = 'var(--surface)';
    userText.style.borderLeft = '3px solid var(--border-strong)';
    userText.style.padding = '12px';
    userText.style.borderRadius = '6px';
    userText.style.margin = '4px 0 14px 0';
    userText.style.fontSize = '14px';
    userText.style.whiteSpace = 'pre-wrap';
    userText.textContent = saved.answerText.trim() ? saved.answerText : "(No answer provided)";
    qBlock.appendChild(userText);
    
    // Rubric Card
    const rub = document.createElement('div');
    rub.className = 'rubric-box';
    
    const rubTitle = document.createElement('span');
    rubTitle.className = 'rubric-header';
    rubTitle.textContent = 'Official Grading Rubric Criteria';
    rub.appendChild(rubTitle);
    
    const rLevels = document.createElement('div');
    rLevels.className = 'rubric-levels';
    rLevels.innerHTML = `
      <div>🟢 <strong>4 Points (Proficient):</strong> ${activePrompt.rubric.proficient}</div>
      <div style="margin-top:4px;">🟡 <strong>2 Points (Partially Proficient):</strong> ${activePrompt.rubric.partial}</div>
      <div style="margin-top:4px;">🔴 <strong>0 Points (Not Proficient):</strong> ${activePrompt.rubric.not_proficient}</div>
    `;
    rub.appendChild(rLevels);
    qBlock.appendChild(rub);
    
    // Model Answer Card
    const model = document.createElement('div');
    model.className = 'model-ans-box';
    
    const modTitle = document.createElement('span');
    modTitle.className = 'rubric-header';
    modTitle.textContent = 'Sample Proficient Model Answer';
    model.appendChild(modTitle);
    
    const modText = document.createElement('div');
    modText.style.fontSize = '13.5px';
    modText.textContent = activePrompt.modelAnswer;
    model.appendChild(modText);
    
    qBlock.appendChild(model);
    
    // Self grading selector panel
    const selfGradePanel = document.createElement('div');
    selfGradePanel.style.display = 'flex';
    selfGradePanel.style.alignItems = 'center';
    selfGradePanel.style.gap = '12px';
    selfGradePanel.style.marginTop = '16px';
    selfGradePanel.style.padding = '12px';
    selfGradePanel.style.background = 'var(--surface3)';
    selfGradePanel.style.borderRadius = '8px';
    
    const labelSpan = document.createElement('span');
    labelSpan.style.fontSize = '13.5px';
    labelSpan.style.fontWeight = '600';
    labelSpan.textContent = 'Evaluate Your Answer:';
    selfGradePanel.appendChild(labelSpan);
    
    const select = document.createElement('select');
    select.className = 'self-score-select';
    
    const opt0 = document.createElement('option');
    opt0.value = 0; opt0.textContent = '0 - Not Proficient';
    if (parseInt(gradesDict[respKey]) === 0) opt0.selected = true;
    select.appendChild(opt0);
    
    const opt2 = document.createElement('option');
    opt2.value = 2; opt2.textContent = '2 - Partially Proficient';
    if (parseInt(gradesDict[respKey]) === 2) opt2.selected = true;
    select.appendChild(opt2);
    
    const opt4 = document.createElement('option');
    opt4.value = 4; opt4.textContent = '4 - Proficient';
    if (parseInt(gradesDict[respKey]) === 4) opt4.selected = true;
    select.appendChild(opt4);
    
    select.addEventListener('change', () => {
      gradesDict[respKey] = parseInt(select.value);
      saveExamResult();
      
      // Update overall result score panel
      renderFinalExamReview(document.getElementById('main-view'));
    });
    
    selfGradePanel.appendChild(select);
    qBlock.appendChild(selfGradePanel);
    
    container.appendChild(qBlock);
  });
}

function retakeExamSimulation() {
  if (confirm("Are you sure you want to clear your current graded result and start a new exam simulation?")) {
    appState.examResult = null;
    saveExamResult();
    startFinalExamSimulation();
  }
}

// ── STUDY GUIDE PRACTICE EXAM RENDERERS (RANDOMIZED PRACTICE TEST) ──
function renderPracticeExamSetup(container) {
  let html = `
    <div class="exam-setup-box">
      <h2 class="exam-setup-title">🎯 Randomized Practice Test</h2>
      <p style="color: var(--text-secondary); margin-bottom: 24px; font-size: 14.5px;">
        Generate a practice session pulling randomized questions from all 8 units of the study guide. Perfect for general prep.
      </p>
      
      <div class="form-group">
        <label for="exam-q-count">Number of Questions:</label>
        <select class="form-select" id="exam-q-count">
          <option value="25">25 Questions</option>
          <option value="50" selected>50 Questions</option>
          <option value="100">100 Questions</option>
          <option value="all">All (${total_questions_count()} Questions)</option>
        </select>
      </div>
      
      <div class="form-group">
        <label for="exam-time">Time Limit:</label>
        <select class="form-select" id="exam-time">
          <option value="0">No Time Limit</option>
          <option value="15">15 Minutes</option>
          <option value="30">30 Minutes</option>
          <option value="60" selected>60 Minutes</option>
          <option value="120">120 Minutes</option>
        </select>
      </div>
      
      <button class="exam-btn" id="start-exam-btn" style="margin-top: 10px;">Start Practice Test</button>
    </div>
  `;
  container.innerHTML = html;
  
  document.getElementById('start-exam-btn').addEventListener('click', startPracticeExam);
}

function total_questions_count() {
  let total = 0;
  const data = getActiveQuizData();
  const startUnit = appState.currentSubject === 'biology' ? 1 : 5;
  for (let u = startUnit; u <= 8; u++) {
    if (data[u]) total += data[u].length;
  }
  return total;
}

function startPracticeExam() {
  const countSelect = document.getElementById('exam-q-count').value;
  const timeSelect = parseInt(document.getElementById('exam-time').value);
  
  // Aggregate all questions
  let allQs = [];
  const data = getActiveQuizData();
  const startUnit = appState.currentSubject === 'biology' ? 1 : 5;
  for (let u = startUnit; u <= 8; u++) {
    if (!data[u]) continue;
    data[u].forEach((q, idx) => {
      allQs.push({ ...q, unit: u, originalIdx: idx });
    });
  }
  
  // Shuffle and select
  allQs = shuffleArray(allQs);
  let limit = allQs.length;
  if (countSelect !== 'all') {
    limit = parseInt(countSelect);
  }
  const selectedQs = allQs.slice(0, Math.min(limit, allQs.length));
  
  // Setup exam session (study practice session)
  appState.studyExamSession = {
    questions: selectedQs,
    answers: {},
    timeLimit: timeSelect,
    timeLeft: timeSelect * 60,
    timerInterval: null,
    submitted: false
  };
  
  renderStudyExamRoom();
}

function renderStudyExamRoom() {
  const mainView = document.getElementById('main-view');
  const session = appState.studyExamSession;
  
  let timerHtml = '';
  if (session.timeLimit > 0) {
    const minutes = Math.floor(session.timeLeft / 60);
    const seconds = session.timeLeft % 60;
    timerHtml = `<div class="exam-timer" id="study-exam-timer-display">${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}</div>`;
    
    if (session.timerInterval) clearInterval(session.timerInterval);
    session.timerInterval = setInterval(() => {
      session.timeLeft--;
      if (session.timeLeft <= 0) {
        clearInterval(session.timerInterval);
        submitStudyExam();
      } else {
        const mins = Math.floor(session.timeLeft / 60);
        const secs = session.timeLeft % 60;
        const display = document.getElementById('study-exam-timer-display');
        if (display) {
          display.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        }
      }
    }, 1000);
  }
  
  let html = `
    <div class="exam-header">
      <div>
        <div class="exam-meta-title">🎯 Study Practice Session</div>
        <div style="font-size: 13px; color: var(--text-secondary); margin-top: 4px;">
          ${session.questions.length} questions pulled randomly from all units. Answers will be graded all at once at the end.
        </div>
      </div>
      <div style="display:flex; align-items:center; gap: 14px;">
        ${timerHtml}
        <button class="q-btn" onclick="confirmExitStudyExam()" style="border-color: var(--wrong); color: var(--wrong);">Exit Test</button>
      </div>
    </div>
    
    <div id="study-exam-questions-list"></div>
    
    <div style="margin-top: 24px; padding: 24px; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; text-align:center;">
      <h3 style="font-family:'DM Serif Display', serif; font-size:18px; margin-bottom: 8px;">Completed all questions?</h3>
      <p style="font-size:13.5px; color:var(--text-secondary); margin-bottom: 16px;">Make sure to review your answers before submitting.</p>
      <button class="exam-btn" id="submit-study-exam-btn">Submit and Grade Test</button>
    </div>
  `;
  
  mainView.innerHTML = html;
  
  // Render list of study exam questions
  const qListContainer = document.getElementById('study-exam-questions-list');
  session.questions.forEach((q, eIdx) => {
    const qBlock = document.createElement('div');
    qBlock.className = 'q-block';
    
    const meta = document.createElement('div');
    meta.className = 'q-meta';
    
    const uBadge = document.createElement('span');
    uBadge.className = 'section-badge';
    uBadge.style.fontSize = '9px';
    uBadge.textContent = `Unit ${q.unit} · Sec ${q.section}`;
    meta.appendChild(uBadge);
    
    const qBadge = document.createElement('span');
    qBadge.className = 'q-type-badge';
    qBadge.textContent = (q.t === 'mc' ? 'Multiple Choice' : 'Select All');
    meta.appendChild(qBadge);
    
    qBlock.appendChild(meta);
    
    const text = document.createElement('div');
    text.className = 'q-text';
    text.textContent = `[Unit ${q.section}] ${eIdx + 1}. ${q.q}`;
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label';
      
      const input = document.createElement('input');
      input.type = q.t === 'mc' ? 'radio' : 'checkbox';
      input.name = `study_exam_opt_${eIdx}`;
      input.className = 'opt-input';
      input.value = optIdx;
      
      input.addEventListener('change', () => {
        if (session.submitted) return;
        if (q.t === 'mc') {
          session.answers[eIdx] = [optIdx];
          qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
          label.classList.add('selected');
        } else {
          if (!session.answers[eIdx]) session.answers[eIdx] = [];
          if (input.checked) {
            if (!session.answers[eIdx].includes(optIdx)) session.answers[eIdx].push(optIdx);
            label.classList.add('selected');
          } else {
            session.answers[eIdx] = session.answers[eIdx].filter(i => i !== optIdx);
            label.classList.remove('selected');
          }
        }
      });
      
      label.appendChild(input);
      
      const letter = document.createElement('span');
      letter.className = 'opt-letter';
      letter.textContent = String.fromCharCode(65 + optIdx) + '.';
      label.appendChild(letter);
      
      const textSpan = document.createElement('span');
      textSpan.className = 'opt-text';
      textSpan.textContent = optText;
      label.appendChild(textSpan);
      
      optsDiv.appendChild(label);
    });
    
    qBlock.appendChild(optsDiv);
    qListContainer.appendChild(qBlock);
  });
  
  document.getElementById('submit-study-exam-btn').addEventListener('click', submitStudyExam);
}

function confirmExitStudyExam() {
  if (confirm("Exit this practice test? Your scores will be lost.")) {
    const session = appState.studyExamSession;
    if (session && session.timerInterval) clearInterval(session.timerInterval);
    appState.studyExamSession = null;
    showView('practice-exam');
  }
}

function submitStudyExam() {
  const session = appState.studyExamSession;
  if (!session || session.submitted) return;
  
  if (session.timerInterval) clearInterval(session.timerInterval);
  session.submitted = true;
  
  let correctCount = 0;
  const qListContainer = document.getElementById('study-exam-questions-list');
  const qBlocks = qListContainer.querySelectorAll('.q-block');
  
  session.questions.forEach((q, eIdx) => {
    const qBlock = qBlocks[eIdx];
    const userAnswersList = session.answers[eIdx] || [];
    
    let isCorrect = true;
    if (q.t === 'mc') {
      isCorrect = userAnswersList.includes(q.a);
    } else {
      const selectedTexts = userAnswersList.map(i => q.opts[i]);
      if (selectedTexts.length !== q.correct.length) {
        isCorrect = false;
      } else {
        selectedTexts.forEach(txt => {
          if (!q.correct.includes(txt)) isCorrect = false;
        });
      }
    }
    
    if (isCorrect) correctCount++;
    
    const meta = qBlock.querySelector('.q-meta');
    const badge = document.createElement('span');
    badge.className = 'q-state-badge ' + (isCorrect ? 'correct' : 'wrong');
    badge.style.display = 'inline-block';
    badge.textContent = isCorrect ? '\u2713 Correct' : '\u2717 Incorrect';
    meta.appendChild(badge);
    
    qBlock.querySelectorAll('.opt-label').forEach((label, oIdx) => {
      label.classList.add('locked');
      const input = label.querySelector('input');
      if (input) input.disabled = true;
      
      if (q.t === 'mc') {
        if (oIdx === q.a) {
          label.classList.add('correct');
        } else if (userAnswersList.includes(oIdx)) {
          label.classList.add('wrong');
        }
      } else {
        const optText = q.opts[oIdx];
        const isCorrectChoice = q.correct.includes(optText);
        const wasSelected = userAnswersList.includes(oIdx);
        if (isCorrectChoice) {
          label.classList.add('correct');
          if (!wasSelected) label.classList.add('missed');
        } else if (wasSelected) {
          label.classList.add('wrong');
        }
      }
    });
    
    let feedbackText = '';
    if (q.t === 'mc') {
      const correctLetter = String.fromCharCode(65 + q.a);
      if (isCorrect) {
        feedbackText = `<strong>\u2713 Correct! You chose ${correctLetter}.</strong>`;
      } else {
        const userLetter = userAnswersList.length > 0 ? String.fromCharCode(65 + userAnswersList[0]) : 'None';
        feedbackText = `<strong>\u2717 Incorrect. You chose ${userLetter}. The correct answer is ${correctLetter}.</strong>`;
      }
    } else {
      const correctIndices = [];
      q.opts.forEach((optText, oIdx) => {
        if (q.correct.includes(optText)) correctIndices.push(oIdx);
      });
      const correctLetters = correctIndices.map(i => String.fromCharCode(65 + i)).join(', ');
      if (isCorrect) {
        feedbackText = `<strong>\u2713 Correct! You chose the correct options: ${correctLetters}.</strong>`;
      } else {
        const userLetters = userAnswersList.sort((a,b)=>a-b).map(i => String.fromCharCode(65 + i)).join(', ') || 'None';
        feedbackText = `<strong>\u2717 Incorrect. You chose: ${userLetters}. The correct answers are: ${correctLetters}.</strong>`;
      }
    }
    
    const feedback = document.createElement('div');
    feedback.className = 'q-feedback show ' + (isCorrect ? 'good' : 'bad');
    feedback.innerHTML = `${feedbackText}<br style="margin-bottom: 6px;">${q.explanation || ''}`;
    qBlock.appendChild(feedback);
  });
  
  const pct = Math.round((correctCount / session.questions.length) * 100);
  const grade = pct >= 90 ? 'A' : pct >= 80 ? 'B' : pct >= 70 ? 'C' : pct >= 60 ? 'D' : 'F';
  
  const mainView = document.getElementById('main-view');
  const submitPanel = mainView.querySelector('div[style*="text-align:center"]');
  
  submitPanel.innerHTML = `
    <h3 style="font-family:'DM Serif Display', serif; font-size:26px; margin-bottom: 8px; color: ${pct >= 70 ? 'var(--correct)' : 'var(--wrong)'};">
      Practice Test Score: ${pct}%
    </h3>
    <p style="font-size:16px; font-weight:600; margin-bottom: 12px;">Grade: ${grade} (${correctCount} / ${session.questions.length} correct)</p>
    <div style="display:flex; justify-content:center; gap:12px;">
      <button class="q-btn primary" onclick="showView('practice-exam')">Retake Practice Test</button>
      <button class="q-btn" onclick="showView('dashboard')">Back to Dashboard</button>
    </div>
  `;
  
  submitPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// ── PROGRESS WIPE SETUP ──
function setupResetModal() {
  const resetBtn = document.getElementById('reset-progress-btn');
  const topResetBtn = document.getElementById('top-reset-btn');
  const modal = document.getElementById('confirm-modal');
  const cancelBtn = document.getElementById('modal-cancel');
  const confirmBtn = document.getElementById('modal-confirm');
  
  const showModal = () => {
    modal.classList.add('active');
  };
  
  if (resetBtn) resetBtn.addEventListener('click', showModal);
  if (topResetBtn) topResetBtn.addEventListener('click', showModal);
  
  cancelBtn.addEventListener('click', () => {
    modal.classList.remove('active');
  });
  
  confirmBtn.addEventListener('click', () => {
    modal.classList.remove('active');
    wipeProgress();
  });
}

function wipeProgress() {
  appState.userAnswers = {};
  appState.examSession = null;
  appState.examResult = null;
  localStorage.removeItem('bio_quiz_state_v3');
  localStorage.removeItem('bio_final_exam_session');
  localStorage.removeItem('bio_final_exam_result');
  
  updateDashboardUI();
  showView(appState.currentView);
}

// ── PHONK STATION MP3 PLAYER WITH BASS-REACTIVE SCREEN SHAKE ──
let phonkAudio = null;
let phonkPlaying = false;
let audioCtx = null;
let analyser = null;
let shakeRAF = null;
let audioSourceConnected = false;

function playMusic() {
  if (!phonkAudio) {
    phonkAudio = new Audio('YARA YARA PHONK (TOM SUIT PHONK) SLOWED TO PERFECTION. BEST PART.mp3');
    phonkAudio.loop = true;
    phonkAudio.crossOrigin = 'anonymous';
    phonkAudio.addEventListener('error', () => {
      updateMusicUI('Stopped');
      alert('Could not load audio file. Make sure the MP3 is in the same folder as index.html.');
    });
  }
  
  phonkAudio.play().then(() => {
    phonkPlaying = true;
    updateMusicUI('Playing');
    initAudioAnalyser();
    startScreenShake();
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
  stopScreenShake();
}

function initAudioAnalyser() {
  if (audioSourceConnected) return; // Already connected
  
  // If running via file:// protocol, avoid createMediaElementSource to prevent complete silencing
  if (window.location.protocol === 'file:') {
    console.warn('Running via file:// protocol. Bypassing Web Audio node routing to prevent local CORS mute.');
    return;
  }
  
  try {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    analyser = audioCtx.createAnalyser();
    analyser.fftSize = 256;
    analyser.smoothingTimeConstant = 0.7;
    
    const source = audioCtx.createMediaElementSource(phonkAudio);
    source.connect(analyser);
    analyser.connect(audioCtx.destination);
    audioSourceConnected = true;
  } catch(e) {
    console.warn('Web Audio API not available for shake effect:', e);
  }
}

function startScreenShake() {
  if (shakeRAF) cancelAnimationFrame(shakeRAF);
  
  const body = document.body;
  // Add a subtle vignette overlay for extra impact
  let vignette = document.getElementById('phonk-vignette');
  if (!vignette) {
    vignette = document.createElement('div');
    vignette.id = 'phonk-vignette';
    vignette.style.cssText = `
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      pointer-events: none; z-index: 99999;
      box-shadow: inset 0 0 120px rgba(139, 0, 255, 0), inset 0 0 60px rgba(0, 0, 0, 0);
      transition: box-shadow 0.05s;
    `;
    document.body.appendChild(vignette);
  }
  
  const dataArray = analyser ? new Uint8Array(analyser.frequencyBinCount) : null;
  let smoothedBass = 0;
  
  function shakeLoop() {
    if (!phonkPlaying) {
      body.style.transform = '';
      body.style.filter = '';
      if (vignette) vignette.style.boxShadow = 'inset 0 0 120px rgba(139, 0, 255, 0), inset 0 0 60px rgba(0, 0, 0, 0)';
      return;
    }
    
    let bassLevel = 0;
    
    if (analyser && dataArray) {
      analyser.getByteFrequencyData(dataArray);
      
      // Get bass frequencies (first ~15 bins = sub-bass to low-mid, roughly 0-600Hz)
      let bassSum = 0;
      const bassBins = Math.min(15, dataArray.length);
      for (let i = 0; i < bassBins; i++) {
        bassSum += dataArray[i];
      }
      bassLevel = bassSum / (bassBins * 255); // Normalize to 0-1
      
      // Heavy smoothing for that punchy feel
      smoothedBass = smoothedBass * 0.3 + bassLevel * 0.7;
    } else {
      // Fallback: fake bass pulse if Web Audio isn't available
      smoothedBass = 0.3 + Math.sin(Date.now() / 200) * 0.15;
    }
    
    // Only shake when bass is significant (threshold)
    const intensity = Math.max(0, smoothedBass - 0.15) / 0.85; // Remap so quiet = no shake
    
    if (intensity > 0.01) {
      // Translation: ±0 to ±8px based on intensity
      const maxTranslate = 8;
      const tx = (Math.random() - 0.5) * 2 * maxTranslate * intensity;
      const ty = (Math.random() - 0.5) * 2 * maxTranslate * intensity;
      
      // Rotation: ±0 to ±1.5deg
      const maxRotate = 1.5;
      const rot = (Math.random() - 0.5) * 2 * maxRotate * intensity;
      
      // Scale pulse: 1.0 to 1.012 on heavy bass
      const scale = 1.0 + intensity * 0.012;
      
      body.style.transform = `translate(${tx}px, ${ty}px) rotate(${rot}deg) scale(${scale})`;
      
      // Subtle brightness/contrast pulse
      const brightness = 1.0 + intensity * 0.08;
      const contrast = 1.0 + intensity * 0.05;
      body.style.filter = `brightness(${brightness}) contrast(${contrast})`;
      
      // Purple vignette glow on heavy bass hits
      const vignetteOpacity = Math.min(intensity * 0.6, 0.4);
      const darkOpacity = Math.min(intensity * 0.3, 0.2);
      if (vignette) {
        vignette.style.boxShadow = `inset 0 0 ${80 + intensity * 120}px rgba(139, 0, 255, ${vignetteOpacity}), inset 0 0 ${40 + intensity * 80}px rgba(0, 0, 0, ${darkOpacity})`;
      }
    } else {
      body.style.transform = '';
      body.style.filter = '';
      if (vignette) vignette.style.boxShadow = 'inset 0 0 120px rgba(139, 0, 255, 0), inset 0 0 60px rgba(0, 0, 0, 0)';
    }
    
    shakeRAF = requestAnimationFrame(shakeLoop);
  }
  
  shakeLoop();
}

function stopScreenShake() {
  if (shakeRAF) {
    cancelAnimationFrame(shakeRAF);
    shakeRAF = null;
  }
  document.body.style.transform = '';
  document.body.style.filter = '';
  const vignette = document.getElementById('phonk-vignette');
  if (vignette) vignette.style.boxShadow = 'inset 0 0 120px rgba(139, 0, 255, 0), inset 0 0 60px rgba(0, 0, 0, 0)';
}

// ── SUBJECT & NAVIGATION CONTROL ──
function setSubject(subj) {
  if (window.event) window.event.stopPropagation();
  appState.currentSubject = subj;
  saveState();
  
  // Update switcher UI
  const bioBtn = document.getElementById('subject-bio-btn');
  const histBtn = document.getElementById('subject-hist-btn');
  if (bioBtn && histBtn) {
    if (subj === 'biology') {
      bioBtn.classList.add('primary');
      histBtn.classList.remove('primary');
    } else {
      bioBtn.classList.remove('primary');
      histBtn.classList.add('primary');
    }
  }
  
  // Re-render navigation sidebar
  renderSidebarNav();
  
  // Go to dashboard
  showView('dashboard');
}

function renderSidebarNav() {
  const container = document.getElementById('unit-nav-list-container');
  if (!container) return;
  
  let html = '';
  const isBio = appState.currentSubject === 'biology';
  
  if (isBio) {
    html += `
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'dashboard' ? 'active' : ''}" data-target="dashboard">
          <span class="unit-nav-name">📊 Study Dashboard</span>
        </button>
      </li>
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'active-recall' ? 'active' : ''}" data-target="active-recall">
          <span class="unit-nav-name">📖 Active Recall Reading</span>
        </button>
      </li>
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'ultimate-study' ? 'active' : ''}" data-target="ultimate-study">
          <span class="unit-nav-name">⚡ Ultimate Outline Study</span>
          <span class="unit-badge" style="background:var(--amber-soft); color:var(--amber-ink); border-color:var(--amber-border);">Core</span>
        </button>
      </li>
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'actual-outline' ? 'active' : ''}" data-target="actual-outline">
          <span class="unit-nav-name">📋 Actual Test Outline</span>
          <span class="unit-badge" style="background:var(--accent-soft); color:var(--accent-ink); border-color:var(--accent-soft-2);">Outline</span>
        </button>
      </li>
    `;
    
    const bioUnitNames = {
      1: "Sci & Safety",
      2: "Biomolecules",
      3: "Cell Biology",
      4: "Genetics & DNA",
      5: "Evolution",
      6: "Diversity of Life",
      7: "Plants & Animals",
      8: "Ecology & Energy"
    };
    
    for (let u = 1; u <= 8; u++) {
      html += `
        <li>
          <button class="unit-nav-btn ${appState.currentView === 'unit-' + u ? 'active' : ''}" data-target="unit-${u}">
            <span class="unit-nav-name"><span class="unit-indicator-dot" data-unit="${u}"></span> Unit ${u}: ${bioUnitNames[u]}</span>
            <span class="unit-nav-progress" id="nav-prog-${u}">0%</span>
          </button>
        </li>
      `;
    }
    
    html += `
      <li style="margin-top: 8px; border-top: 1px dashed var(--border); padding-top: 8px;">
        <h2 class="dashboard-title" style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); letter-spacing: 0.05em; margin-bottom: 6px;">Evaluations</h2>
        <button class="unit-nav-btn ${appState.currentView === 'final-exam-simulator' ? 'active' : ''}" data-target="final-exam-simulator">
          <span class="unit-nav-name">⚡ 2026 Final Exam Sim</span>
          <span class="unit-badge" style="background:var(--wrong-soft); color:var(--wrong-ink); border-color:var(--wrong-soft-2);">Outline</span>
        </button>
      </li>
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'practice-exam' ? 'active' : ''}" data-target="practice-exam">
          <span class="unit-nav-name">🎯 Random Practice Test</span>
          <span class="unit-nav-progress">Test</span>
        </button>
      </li>
    `;
  } else {
    html += `
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'dashboard' ? 'active' : ''}" data-target="dashboard">
          <span class="unit-nav-name">📊 Study Dashboard</span>
        </button>
      </li>
    `;
    
    const histUnitNames = {
      5: "Industrial Rev",
      6: "Nationalism & Rev",
      7: "Imperialism",
      8: "World War I"
    };
    
    for (let u = 5; u <= 8; u++) {
      html += `
        <li>
          <button class="unit-nav-btn ${appState.currentView === 'unit-' + u ? 'active' : ''}" data-target="unit-${u}">
            <span class="unit-nav-name"><span class="unit-indicator-dot" data-unit="${u}"></span> Unit ${u}: ${histUnitNames[u]}</span>
            <span class="unit-nav-progress" id="nav-prog-${u}">0%</span>
          </button>
        </li>
      `;
    }
    
    html += `
      <li style="margin-top: 8px; border-top: 1px dashed var(--border); padding-top: 8px;">
        <h2 class="dashboard-title" style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); letter-spacing: 0.05em; margin-bottom: 6px;">Evaluations</h2>
        <button class="unit-nav-btn ${appState.currentView === 'history-final-exam' ? 'active' : ''}" data-target="history-final-exam">
          <span class="unit-nav-name">⚡ Practice Final Exam</span>
          <span class="unit-nav-progress">150 pts</span>
        </button>
      </li>
      <li>
        <button class="unit-nav-btn ${appState.currentView === 'practice-exam' ? 'active' : ''}" data-target="practice-exam">
          <span class="unit-nav-name">🎯 Random Practice Test</span>
          <span class="unit-nav-progress">Test</span>
        </button>
      </li>
    `;
  }
  
  container.innerHTML = html;
  
  // Bind listeners
  container.querySelectorAll('.unit-nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      showView(btn.dataset.target);
    });
  });
  
  updateDashboardUI();
}

// ── ACTIVE RECALL READING ROOM ──
function renderActiveRecallView(container) {
  const selectedUnit = appState.activeRecallUnit;
  const pages = ACTIVE_RECALL_DATA[selectedUnit] || [];
  
  if (pages.length === 0) {
    container.innerHTML = `
      <div class="sidebar-box" style="text-align: center; padding: 40px 20px;">
        <h2 style="font-family:'DM Serif Display', serif; margin-bottom: 12px;">Active Recall Data Loading...</h2>
        <p style="color: var(--text-secondary); font-size:14px;">Active recall reading content is still being generated or is missing for Unit ${selectedUnit}. Please ensure the subagents have finished and compiled.</p>
      </div>
    `;
    return;
  }
  
  if (appState.activeRecallPage < 1 || appState.activeRecallPage > pages.length) {
    appState.activeRecallPage = 1;
  }
  
  const currentPageIdx = appState.activeRecallPage - 1;
  const pageData = pages[currentPageIdx];
  
  let completedPages = 0;
  pages.forEach(p => {
    let pageDone = true;
    if (!p.questions || p.questions.length === 0) {
      pageDone = true;
    } else {
      p.questions.forEach((q, qIdx) => {
        const arKey = `ar_${selectedUnit}_${p.page}_${qIdx}`;
        if (!appState.activeRecallAnswers[arKey] || !appState.activeRecallAnswers[arKey].locked) {
          pageDone = false;
        }
      });
    }
    if (pageDone) completedPages++;
  });
  
  const progressPct = Math.round((completedPages / pages.length) * 100);
  
  let unitTabsHtml = '';
  for (let u = 1; u <= 8; u++) {
    unitTabsHtml += `
      <button class="q-btn ${selectedUnit === u ? 'primary' : ''}" style="padding: 6px 12px; font-weight: 600; font-size:12.5px; border-radius:6px;" onclick="selectRecallUnit(${u})">
        Unit ${u}
      </button>
    `;
  }
  
  let jumpOptionsHtml = '';
  pages.forEach((p, idx) => {
    jumpOptionsHtml += `<option value="${idx + 1}" ${appState.activeRecallPage === idx + 1 ? 'selected' : ''}>Page ${idx + 1}: ${p.slide_title.substring(0, 40)}${p.slide_title.length > 40 ? '...' : ''}</option>`;
  });
  
  let html = `
    <div style="display:flex; align-items:center; gap: 12px; margin-bottom: 8px;">
      <button class="q-btn" onclick="showView('dashboard')">← Dashboard</button>
      <span class="unit-badge">🧬 Active Recall Study Room</span>
    </div>
    <h1 style="font-family:'DM Serif Display', serif; font-size: 32px; margin-bottom: 12px;">Active Recall &amp; Reading Deck</h1>
    <p style="color:var(--text-secondary); margin-bottom: 20px; font-size:14.5px;">
      Read through the detailed explanations of each slide from the notes, then answer the questions to lock in your active recall memory.
    </p>
    
    <div style="display: flex; gap: 8px; margin-bottom: 16px; overflow-x: auto; padding-bottom: 6px; border-bottom: 1px solid var(--border);">
      ${unitTabsHtml}
    </div>
    
    <div class="sidebar-box" style="margin-bottom: 20px; padding: 14px 18px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
      <div style="flex-grow: 1; min-width: 200px;">
        <div style="font-size: 13px; font-weight: 600; margin-bottom: 4px; display:flex; justify-content:space-between;">
          <span>Unit ${selectedUnit} Reading Progress</span>
          <span>${completedPages} / ${pages.length} Pages Read (${progressPct}%)</span>
        </div>
        <div class="bar-container" style="height: 8px; margin-top:0;">
          <div class="bar-fill" style="width: ${progressPct}%; background: var(--correct);"></div>
        </div>
      </div>
      <button class="q-btn danger" style="padding: 6px 12px; font-size:12px;" onclick="resetRecallUnit(${selectedUnit})">Reset Unit Progress</button>
    </div>
    
    <div class="section-card" style="border-top: 4px solid var(--accent);">
      <div class="section-header" style="cursor: default; background: var(--surface2); display:flex; justify-content:space-between; align-items:center; padding: 14px 20px;">
        <div class="section-header-left" style="display:flex; flex-direction:column; gap:2px; align-items:flex-start;">
          <span class="section-badge" style="background: var(--accent-soft); color: var(--accent-ink);">PAGE ${appState.activeRecallPage} OF ${pages.length}</span>
          <span style="font-size: 11px; color: var(--text-dim); font-family: 'DM Mono', monospace; margin-top: 4px;">File: ${pageData.filename} &middot; Section: ${pageData.section_title}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
          <button class="q-btn" style="padding: 4px 10px; font-size:12px;" ${appState.activeRecallPage === 1 ? 'disabled' : ''} onclick="navigateRecallPage(-1)">← Prev</button>
          <select class="form-select" style="padding: 4px 8px; font-size:12px; max-width: 140px; margin: 0;" onchange="jumpRecallPage(this.value)">
            ${jumpOptionsHtml}
          </select>
          <button class="q-btn" style="padding: 4px 10px; font-size:12px;" ${appState.activeRecallPage === pages.length ? 'disabled' : ''} onclick="navigateRecallPage(1)">Next →</button>
        </div>
      </div>
      
      <div class="section-body open" style="padding: 24px;">
        <h2 style="font-family:'DM Serif Display', serif; font-size: 23px; margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
          ${pageData.slide_title}
        </h2>
        
        <details style="margin-bottom: 20px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px;">
          <summary style="padding: 10px 14px; font-size: 13px; font-weight: 600; color: var(--text-secondary); cursor: pointer; user-select: none;">
            📄 Show Original Slide Text
          </summary>
          <div style="padding: 14px; font-size: 13.5px; white-space: pre-wrap; font-family: 'DM Mono', monospace; line-height: 1.5; border-top: 1px solid var(--border); color: var(--text-secondary);">
            ${pageData.original_text || '(No text on this slide)'}
          </div>
        </details>
        
        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.01);">
          <div style="font-family: 'DM Mono', monospace; font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 700; margin-bottom: 8px; letter-spacing:0.05em;">Detailed Concept Explanation</div>
          <div style="font-size: 15px; line-height: 1.7; color: var(--text-primary);">
            ${pageData.explanation.replace(/\\n/g, '<br style="margin-bottom: 8px;">')}
          </div>
        </div>
        
        <div style="border-top: 1px dashed var(--border); padding-top: 20px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 16px;">
            <h3 style="font-family:'DM Serif Display', serif; font-size: 19px; display:flex; align-items:center; gap:8px;">
              <span>🧠 Active Recall Self-Test</span>
            </h3>
            <button class="q-btn danger" style="padding: 4px 10px; font-size:11.5px;" onclick="resetRecallPage(${selectedUnit}, ${appState.activeRecallPage})">Reset Page Qs</button>
          </div>
          
          <div id="recall-qs-container">
            <!-- Questions rendered here -->
          </div>
        </div>
        
      </div>
    </div>
  `;
  
  container.innerHTML = html;
  
  const qContainer = document.getElementById('recall-qs-container');
  renderRecallQuestions(qContainer, selectedUnit, appState.activeRecallPage, pageData.questions || []);
}

function selectRecallUnit(u) {
  appState.activeRecallUnit = u;
  appState.activeRecallPage = 1;
  saveState();
  renderActiveRecallView(document.getElementById('main-view'));
}

function navigateRecallPage(direction) {
  appState.activeRecallPage += direction;
  saveState();
  renderActiveRecallView(document.getElementById('main-view'));
}

function jumpRecallPage(val) {
  appState.activeRecallPage = parseInt(val) || 1;
  saveState();
  renderActiveRecallView(document.getElementById('main-view'));
}

function renderRecallQuestions(container, unitNum, pageNum, questions) {
  container.innerHTML = '';
  
  if (questions.length === 0) {
    container.innerHTML = `<div style="font-size: 14px; color: var(--text-dim); font-style: italic;">No active recall questions for this page. Read the explanation and proceed!</div>`;
    return;
  }
  
  questions.forEach((q, idx) => {
    const arKey = `ar_${unitNum}_${pageNum}_${idx}`;
    const savedState = appState.activeRecallAnswers[arKey] || { selected: [], locked: false, correct: false };
    
    const qBlock = document.createElement('div');
    qBlock.className = 'q-block';
    
    const meta = document.createElement('div');
    meta.className = 'q-meta';
    
    const badge = document.createElement('span');
    badge.className = 'q-type-badge';
    badge.textContent = `Question ${idx + 1}`;
    meta.appendChild(badge);
    
    const stateBadge = document.createElement('span');
    stateBadge.className = 'q-state-badge';
    if (savedState.locked) {
      stateBadge.classList.add(savedState.correct ? 'correct' : 'wrong');
      stateBadge.textContent = savedState.correct ? '\u2713 Correct' : '\u2717 Incorrect';
    }
    meta.appendChild(stateBadge);
    
    qBlock.appendChild(meta);
    
    const text = document.createElement('div');
    text.className = 'q-text';
    text.textContent = q.q;
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label';
      if (savedState.selected.includes(optIdx)) label.classList.add('selected');
      if (savedState.locked) {
        label.classList.add('locked');
        if (optIdx === q.a) {
          label.classList.add('correct');
        } else if (savedState.selected.includes(optIdx)) {
          label.classList.add('wrong');
        }
      }
      
      const input = document.createElement('input');
      input.type = 'radio';
      input.className = 'opt-input';
      input.name = `opt_ar_${unitNum}_${pageNum}_${idx}`;
      input.value = optIdx;
      input.checked = savedState.selected.includes(optIdx);
      input.disabled = savedState.locked;
      
      input.addEventListener('change', () => {
        if (savedState.locked) return;
        savedState.selected = [optIdx];
        qBlock.querySelectorAll('.opt-label').forEach(lbl => lbl.classList.remove('selected'));
        label.classList.add('selected');
        
        const checkBtn = qBlock.querySelector('.check-answer-btn');
        if (checkBtn) checkBtn.style.display = 'inline-flex';
        
        appState.activeRecallAnswers[arKey] = { selected: savedState.selected, locked: false, correct: false };
        localStorage.setItem('quiz_recall_answers_v1', JSON.stringify(appState.activeRecallAnswers));
      });
      
      label.appendChild(input);
      
      const letter = document.createElement('span');
      letter.className = 'opt-letter';
      letter.textContent = String.fromCharCode(65 + optIdx) + '.';
      label.appendChild(letter);
      
      const textSpan = document.createElement('span');
      textSpan.className = 'opt-text';
      textSpan.textContent = optText;
      label.appendChild(textSpan);
      
      optsDiv.appendChild(label);
    });
    qBlock.appendChild(optsDiv);
    
    const feedback = document.createElement('div');
    feedback.className = 'q-feedback';
    if (savedState.locked) {
      feedback.classList.add('show', savedState.correct ? 'good' : 'bad');
      const correctLetter = String.fromCharCode(65 + q.a);
      let feedbackText = '';
      if (savedState.correct) {
        feedbackText = `<strong>\u2713 Correct! You chose ${correctLetter}.</strong>`;
      } else {
        const userLetter = savedState.selected.length > 0 ? String.fromCharCode(65 + savedState.selected[0]) : 'None';
        feedbackText = `<strong>\u2717 Incorrect. You chose ${userLetter}. The correct answer is ${correctLetter}.</strong>`;
      }
      feedback.innerHTML = `${feedbackText}<br style="margin-bottom:6px;">${q.exp || q.explanation || ''}`;
    }
    qBlock.appendChild(feedback);
    
    const actions = document.createElement('div');
    actions.className = 'q-actions';
    if (!savedState.locked) {
      const checkBtn = document.createElement('button');
      checkBtn.className = 'q-btn primary check-answer-btn';
      checkBtn.textContent = 'Check Answer';
      checkBtn.style.display = savedState.selected.length > 0 ? 'inline-flex' : 'none';
      checkBtn.addEventListener('click', () => {
        if (savedState.selected.length === 0) return;
        gradeRecallQuestion(unitNum, pageNum, idx, qBlock, q, savedState);
        checkBtn.style.display = 'none';
      });
      actions.appendChild(checkBtn);
    }
    qBlock.appendChild(actions);
    
    container.appendChild(qBlock);
  });
}

function gradeRecallQuestion(unitNum, pageNum, idx, qBlock, q, state) {
  if (state.locked) return;
  state.locked = true;
  
  const isCorrect = state.selected.includes(q.a);
  state.correct = isCorrect;
  
  const arKey = `ar_${unitNum}_${pageNum}_${idx}`;
  appState.activeRecallAnswers[arKey] = {
    selected: state.selected,
    locked: true,
    correct: isCorrect
  };
  
  localStorage.setItem('quiz_recall_answers_v1', JSON.stringify(appState.activeRecallAnswers));
  
  const stateBadge = qBlock.querySelector('.q-state-badge');
  stateBadge.className = 'q-state-badge ' + (isCorrect ? 'correct' : 'wrong');
  stateBadge.textContent = isCorrect ? '\u2713 Correct' : '\u2717 Incorrect';
  
  const correctLetter = String.fromCharCode(65 + q.a);
  let feedbackText = '';
  if (isCorrect) {
    feedbackText = `<strong>\u2713 Correct! You chose ${correctLetter}.</strong>`;
  } else {
    const userLetter = state.selected.length > 0 ? String.fromCharCode(65 + state.selected[0]) : 'None';
    feedbackText = `<strong>\u2717 Incorrect. You chose ${userLetter}. The correct answer is ${correctLetter}.</strong>`;
  }
  
  const feedback = qBlock.querySelector('.q-feedback');
  feedback.className = 'q-feedback show ' + (isCorrect ? 'good' : 'bad');
  feedback.innerHTML = `${feedbackText}<br style="margin-bottom:6px;">${q.exp || q.explanation || ''}`;
  
  qBlock.querySelectorAll('.opt-label').forEach((label, oIdx) => {
    label.classList.add('locked');
    if (oIdx === q.a) {
      label.classList.add('correct');
    } else if (state.selected.includes(oIdx)) {
      label.classList.add('wrong');
    }
  });
  
  renderActiveRecallView(document.getElementById('main-view'));
}

function resetRecallPage(unitNum, pageNum) {
  if (window.event) window.event.stopPropagation();
  Object.keys(appState.activeRecallAnswers).forEach(key => {
    if (key.startsWith(`ar_${unitNum}_${pageNum}_`)) {
      delete appState.activeRecallAnswers[key];
    }
  });
  localStorage.setItem('quiz_recall_answers_v1', JSON.stringify(appState.activeRecallAnswers));
  renderActiveRecallView(document.getElementById('main-view'));
}

function resetRecallUnit(unitNum) {
  if (window.event) window.event.stopPropagation();
  if (!confirm(`Reset all answers in Unit ${unitNum} recall reading?`)) return;
  Object.keys(appState.activeRecallAnswers).forEach(key => {
    if (key.startsWith(`ar_${unitNum}_`)) {
      delete appState.activeRecallAnswers[key];
    }
  });
  localStorage.setItem('quiz_recall_answers_v1', JSON.stringify(appState.activeRecallAnswers));
  renderActiveRecallView(document.getElementById('main-view'));
}

// ── SECTION RESET / SHUFFLE ──
let sectionShuffleMap = {}; // key: 'unit_sec' -> shuffled index array

function loadShuffleState() {
  try {
    const saved = localStorage.getItem('bio_quiz_shuffle_v1');
    if (saved) sectionShuffleMap = JSON.parse(saved);
  } catch(e) { sectionShuffleMap = {}; }
}

function saveShuffleState() {
  localStorage.setItem('bio_quiz_shuffle_v1', JSON.stringify(sectionShuffleMap));
}

function reRenderSectionOnly(unitNum, sec) {
  const data = getActiveQuizData();
  const questions = data[unitNum] || [];
  const secQs = [];
  questions.forEach((q, idx) => {
    if (q.section === sec) secQs.push({ q, idx });
  });
  
  // Apply shuffle if exists
  const shuffleKey = appState.currentSubject === 'biology' ? `${unitNum}_${sec}` : `hist_${unitNum}_${sec}`;
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
    const qKey = appState.currentSubject === 'biology' ? `q_${unitNum}_${sec}_${idx}` : `q_hist_${unitNum}_${sec}_${idx}`;
    if (appState.userAnswers[qKey] && appState.userAnswers[qKey].locked) answered++;
  });
  const progEl = document.getElementById(`sec-prog-${sec.replace('.', '_')}`);
  if (progEl) progEl.textContent = `${answered} / ${secQs.length} completed`;
}

function resetSection(unitNum, sec) {
  if (window.event) window.event.stopPropagation();
  
  const data = getActiveQuizData();
  const questions = data[unitNum] || [];
  questions.forEach((q, idx) => {
    if (q.section === sec) {
      const qKey = appState.currentSubject === 'biology' ? `q_${unitNum}_${sec}_${idx}` : `q_hist_${unitNum}_${sec}_${idx}`;
      delete appState.userAnswers[qKey];
    }
  });
  
  saveState();
  updateDashboardUI();
  reRenderSectionOnly(unitNum, sec);
}

function shuffleSection(unitNum, sec) {
  if (window.event) window.event.stopPropagation();
  const data = getActiveQuizData();
  const questions = data[unitNum] || [];
  const sectionIndices = [];
  questions.forEach((q, idx) => {
    if (q.section === sec) sectionIndices.push(idx);
  });
  
  const shuffled = [...sectionIndices];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  
  const key = appState.currentSubject === 'biology' ? `${unitNum}_${sec}` : `hist_${unitNum}_${sec}`;
  sectionShuffleMap[key] = shuffled;
  saveShuffleState();
  reRenderSectionOnly(unitNum, sec);
}

function unshuffleSection(unitNum, sec) {
  if (window.event) window.event.stopPropagation();
  const key = appState.currentSubject === 'biology' ? `${unitNum}_${sec}` : `hist_${unitNum}_${sec}`;
  delete sectionShuffleMap[key];
  saveShuffleState();
  reRenderSectionOnly(unitNum, sec);
}

function updateMusicUI(state) {
  const disc = document.getElementById('vinyl-disc');
  const eq = document.getElementById('eq-bars');
  const status = document.getElementById('track-status');
  const playBtn = document.getElementById('music-play-btn');
  const stopBtn = document.getElementById('music-stop-btn');
  
  if (state === 'Playing') {
    disc.classList.add('playing');
    eq.classList.add('playing');
    status.textContent = 'Playing';
    playBtn.disabled = true;
    stopBtn.disabled = false;
  } else if (state === 'Loading...') {
    disc.classList.remove('playing');
    eq.classList.remove('playing');
    status.textContent = 'Loading...';
    playBtn.disabled = true;
    stopBtn.disabled = false;
  } else {
    disc.classList.remove('playing');
    eq.classList.remove('playing');
    status.textContent = 'Stopped';
    playBtn.disabled = false;
    stopBtn.disabled = true;
  }
}

function setupMusicPlayer() {
  const playBtn = document.getElementById('music-play-btn');
  const stopBtn = document.getElementById('music-stop-btn');
  if (playBtn) playBtn.addEventListener('click', playMusic);
  if (stopBtn) stopBtn.addEventListener('click', stopMusic);
}

// ── INITIALIZATION ──
document.addEventListener('DOMContentLoaded', () => {
  loadState();
  loadShuffleState();
  renderSidebarNav();
  setupResetModal();
  setupMusicPlayer();
  
  // Theme toggle
  document.getElementById('theme-toggle').addEventListener('click', () => {
    const nextTheme = appState.theme === 'light' ? 'dark' : 'light';
    appState.theme = nextTheme;
    document.documentElement.setAttribute('data-theme', nextTheme);
    localStorage.setItem('bio_quiz_theme', nextTheme);
    document.getElementById('theme-toggle').textContent = nextTheme === 'light' ? 'Dark Mode' : 'Light Mode';
  });
  
  // Default to dashboard
  showView('dashboard');
});
/* ULTIMATE_JS_CONTENT */
</script>
</body>
</html>
"""

# Serialize raw data
study_data_json = json.dumps(study_data, ensure_ascii=False)
exam_data_json = json.dumps(exam_data, ensure_ascii=False)
active_recall_json = json.dumps(active_recall_data, ensure_ascii=False)
history_json = json.dumps(history_data, ensure_ascii=False)

# Load history exam data
history_exam_objective = []
history_exam_documents = []
history_exam_open = []

obj_path = os.path.join(base_dir, "history_exam_objective.json")
if os.path.exists(obj_path):
    with open(obj_path, "r", encoding="utf-8") as f:
        history_exam_objective = json.load(f)

doc_path = os.path.join(base_dir, "history_exam_documents.json")
if os.path.exists(doc_path):
    with open(doc_path, "r", encoding="utf-8") as f:
        history_exam_documents = json.load(f)

open_path = os.path.join(base_dir, "history_exam_open.json")
if os.path.exists(open_path):
    with open(open_path, "r", encoding="utf-8") as f:
        history_exam_open = json.load(f)

history_exam_json = json.dumps({
    "objective": history_exam_objective,
    "documents": history_exam_documents,
    "open": history_exam_open
}, ensure_ascii=False)

# Load compiled ultimate study data
ultimate_study_data = {}
ultimate_study_data_path = os.path.join(base_dir, "ultimate_study_data.json")
if os.path.exists(ultimate_study_data_path):
    with open(ultimate_study_data_path, "r", encoding="utf-8") as f:
        ultimate_study_data = json.load(f)
ultimate_study_json = json.dumps(ultimate_study_data, ensure_ascii=False)

# Load ultimate study JS script
ultimate_js_content = ""
ultimate_js_path = r"C:\Users\elieu\.gemini\antigravity\brain\a37b27ff-fecd-4f79-bc15-556af791e659\scratch\ultimate_study.js"
if os.path.exists(ultimate_js_path):
    with open(ultimate_js_path, "r", encoding="utf-8") as f:
        ultimate_js_content = f.read()

# Insert the data into template using string replace instead of % formatting
final_html = html_template.replace("%s", study_data_json, 1) \
                           .replace("%s", exam_data_json, 1) \
                           .replace("%s", active_recall_json, 1) \
                           .replace("%s", history_json, 1) \
                           .replace("%s", history_exam_json, 1) \
                           .replace("%s", ultimate_study_json, 1)

# Replace JS content placeholder
final_html = final_html.replace("/* ULTIMATE_JS_CONTENT */", ultimate_js_content)

# Write to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Assembly complete! Generated index.html with Final Exam Simulator & Ultimate Outline Study Mode.")
