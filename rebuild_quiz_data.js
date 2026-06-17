const fs = require('fs');
const base = 'C:/Users/elieu/OneDrive/Desktop/biofinaltest/';

// Build QUIZ_DATA from the JSON files (source of truth)
const quizData = {};
for (let u = 1; u <= 8; u++) {
  const qs = JSON.parse(fs.readFileSync(base + 'unit' + u + '_questions.json', 'utf8'));
  quizData[String(u)] = qs;
}

const newQuizDataJs = 'const QUIZ_DATA = ' + JSON.stringify(quizData) + ';';

let html = fs.readFileSync(base + 'index.html', 'utf8');

// Replace the QUIZ_DATA line
const before = html.length;
html = html.replace(/const QUIZ_DATA = \{.*?\};/s, newQuizDataJs);
const after = html.length;

if (html.length === before) {
  console.error('ERROR: QUIZ_DATA pattern not replaced — line endings or format may differ');
  process.exit(1);
}

fs.writeFileSync(base + 'index.html', html);
console.log('QUIZ_DATA rebuilt in index.html (' + (before - after > 0 ? '-' : '+') + Math.abs(after - before) + ' bytes)');

// Quick sanity check
const check = html.match(/const QUIZ_DATA = (\{.*?\});/s);
if (check) {
  const d = JSON.parse(check[1]);
  let total = 0;
  for (let u = 1; u <= 8; u++) total += (d[u] || []).length;
  console.log('Total questions in QUIZ_DATA:', total);
  // Spot check unit3 #0 and unit4 #5
  console.log('unit3[0]:', d['3'][0].q.slice(0, 80));
  console.log('unit4[5]:', d['4'][5].q.slice(0, 80));
  console.log('unit5[2]:', d['5'][2].q.slice(0, 80));
  console.log('unit8[9]:', d['8'][9].q.slice(0, 80));
}
