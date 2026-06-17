const fs = require('fs');
const base = 'C:/Users/elieu/OneDrive/Desktop/biofinaltest/';
for(let u=1;u<=8;u++){
  const qs = JSON.parse(fs.readFileSync(base+'unit'+u+'_questions.json','utf8'));
  qs.forEach((q,i)=>{
    const qtext = q.q.toLowerCase();
    const ans = ((q.opts||[])[q.a]||'').toLowerCase();
    const personAns = /^(gregor mendel|thomas hunt morgan|charles darwin|antonie|anton van|leeuwenhoek|robert hooke|louis pasteur|watson|crick|oswald avery|hershey|rosalind franklin|lamarck|linnaeus|buffon|cuvier|lyell|schwann|schleiden|virchow|redi|griffith|chargaff|meselson|stahl|flemming|count buffon|jean-baptiste|darwin|stanley miller)/i.test(ans);
    const whoQ = /^who /.test(qtext);
    const whenQ = /^(in what year|when was|when did|what year)/i.test(q.q);
    const listQ = /^(name the|list the|list all)/i.test(q.q);
    if(whoQ || personAns || whenQ || listQ){
      console.log('[u'+u+' #'+i+' s='+q.section+'] Q: '+q.q.slice(0,110));
      console.log('  A: '+ans.slice(0,80));
    }
  });
}
