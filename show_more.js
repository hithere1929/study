const fs = require('fs');
const base = 'C:/Users/elieu/OneDrive/Desktop/biofinaltest/';
const targets = [
  ['unit6_questions.json', [24]],
];
targets.forEach(([file, indices]) => {
  const qs = JSON.parse(fs.readFileSync(base+file,'utf8'));
  indices.forEach(i => {
    const q = qs[i];
    console.log('\n['+file+' #'+i+' sec='+q.section+']');
    console.log('Q:', q.q);
    q.opts.forEach((o,j) => console.log(' '+(j===q.a?'*':' ')+'['+j+'] '+o));
  });
});
