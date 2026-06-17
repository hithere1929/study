const fs = require('fs');
const base = 'C:/Users/elieu/OneDrive/Desktop/biofinaltest/';
for(let u=1;u<=8;u++){
  const qs = JSON.parse(fs.readFileSync(base+'unit'+u+'_questions.json','utf8'));
  console.log('\n=== UNIT '+u+' ('+qs.length+' questions) ===');
  qs.forEach((q,i)=>{
    const ans = ((q.opts||[])[q.a]||'');
    console.log('[#'+i+' s='+q.section+'] '+q.q.slice(0,100));
    console.log('  -> '+ans.slice(0,90));
  });
}
