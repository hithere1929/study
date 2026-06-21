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

const HISTORY_OUTLINE_DISTRACTOR_SETS = [
  ["Mainly new laws forcing peasants into factories, with little connection to farming, resources, capital, or markets", "Primarily the invention of electricity and automobiles, which made coal, steam, and textile factories unnecessary", "Mostly caused by Marxist theory and labor unions demanding factory production before industry had expanded"],
  ["A political revolution where workers seized farms and redistributed land equally to stop urban growth", "A factory system change where machines replaced all farm labor without changing crops, breeding, or enclosure", "A transportation change based on canals and railroads that lowered shipping costs but did not increase food supply"],
  ["Invented the first steam engine from scratch and used it mainly to power ocean dreadnoughts", "Discovered coal power and personally created the factory system by replacing all hand labor", "Developed the seed drill and crop rotation methods that caused the Second Agricultural Revolution"],
  ["Made factories smaller and returned most production to home workshops instead of centralized industry", "Reduced the need for coal and iron by shifting transportation back to horses and sailing ships", "Improved communication through telegraphs but had little effect on mines, railroads, steamships, or markets"],
  ["Britain industrialized first mainly because it avoided colonies, banking, ports, and overseas trade", "Britain led because it had no major coal or iron but copied French industry after 1848", "Britain became the center mostly because Parliament forced workers to remain in villages instead of cities"],
  ["Ended class conflict by immediately improving wages, removing slums, and eliminating pollution", "Kept most people in rural villages and prevented the growth of factory towns and mass production", "Only changed transportation and had almost no effect on families, social classes, ideology, or reform"],
  ["A change in political voting rights that allowed workers to elect members of Parliament", "A farming reform based on enclosure, seed drills, crop rotation, and selective breeding", "A military alliance system that moved armies faster but did not affect markets or consumer goods"],
  ["A slow movement of factory owners into the countryside to avoid city crowding and pollution", "A planned reform that created clean, healthy cities before workers moved there", "A decline in cities caused by enclosure ending and peasants returning to village farming"],
  ["A socialist theory arguing that workers should overthrow factory owners and abolish private property", "A conservative belief that monarchs and aristocrats should control production to protect social order", "A reform movement demanding temperance, suffrage, and moral domestic leadership by women"],
  ["A free-market theory claiming competition and private property naturally benefit society through the invisible hand", "A conservative defense of monarchy, church authority, and aristocratic privilege against liberal reform", "A nationalist argument that people with shared language and culture should form their own state"],
  ["Work became more independent and flexible because machines let families produce goods at home", "Factory work generally meant short hours, high wages, safe conditions, and little supervision", "Most city work shifted away from wage labor and toward unpaid agricultural service on estates"],
  ["Small family workshops that avoided outside investors and prevented any company from controlling a market", "Government-owned farms that used monopoly power to distribute food equally to factory workers", "Labor unions that controlled all wages and forced owners to share profits with workers"],
  ["A working-class movement that demanded women enter factories and replace men as public wage earners", "A scientific theory claiming domestic labor made women biologically superior to men in politics", "An imperial policy that placed European women in colonies to spread missionary education"],
  ["Women mainly led violent factory strikes and rejected political reforms like voting rights", "Women used reform movements only to defend alcohol sales and keep politics male-dominated", "Women avoided public activism because the Cult of Domesticity permanently excluded them from reform"],
  ["Accurate biological science proving that poverty and empire were natural and morally fair", "A socialist theory arguing all races and classes should be made economically equal by revolution", "A liberal reform idea claiming legal equality would end imperialism and racial hierarchy immediately"],
  ["Conservatives wanted written constitutions and civil liberties, while liberals defended absolute monarchy", "Both groups wanted the same thing: monarchy, aristocracy, church power, and no voting rights", "Liberals mainly supported empire overseas, while conservatives focused only on industrial labor reform"],
  ["Loyalty to a monarch or dynasty regardless of language, culture, ethnicity, or shared history", "A belief that industrial workers should unite internationally instead of caring about national identity", "A diplomatic system designed to prevent any one country from becoming too powerful after Napoleon"],
  ["A nationalist congress that created Germany and Italy as unified nation-states", "A liberal revolution that expanded voting rights and constitutional government across Europe", "A meeting where European powers divided Africa and created rules for imperial conquest"],
  ["France was stable because the restored monarchy satisfied liberals, workers, and conservatives equally", "France's crises came only from foreign invasion, not voting rights, class conflict, or economic problems", "France had already solved revolutionary tensions by permanently accepting Napoleon's empire"],
  ["A monarchy restored by the Congress of Vienna with Louis XVIII ruling as an absolute king", "A socialist government led by the Paris Commune after France lost to Prussia", "A nationalist republic ruled by Bismarck after the Franco-Prussian War"],
  ["A Mexican priest who began independence by calling peasants to revolt against Spanish rule", "A South American creole who liberated northern South America through campaigns against Spain", "A French emperor who restored slavery and peacefully negotiated Haitian independence"],
  ["Mexico gained independence when Spain voluntarily granted it after the Congress of Vienna", "Mexico was freed by Simon Bolivar's armies after they crossed from northern South America", "Mexico became independent through British imperial pressure after the Opium War opened trade"],
  ["Leader of Mexico's independence who completed the revolt by creating a conservative monarchy", "Former enslaved Haitian general who organized the revolution against French colonial slavery", "Italian nationalist who led Red Shirts in southern Italy and handed territory to Victor Emmanuel II"],
  ["A fully unified German empire created by Bismarck after defeating France in 1871", "A liberal parliament that successfully unified Germany through speeches and majority votes", "A military alliance created by William II to prepare Germany for World War I"],
  ["A liberal idealist who rejected war and unified Germany through moral arguments and popular voting", "An Austrian conservative who used the Congress of Vienna to stop German nationalism permanently", "A French emperor who lost power after the Franco-Prussian War and the fall of Paris"],
  ["He relied only on democratic elections and avoided war, diplomacy, or military expansion", "He strengthened Austria and France so Prussia would remain one German state among many equals", "He unified Germany by supporting Italian nationalists and giving power to the Catholic Church"],
  ["William II removed him because Bismarck wanted aggressive colonies and a huge navy too quickly", "William II removed him because Bismarck supported socialist revolution and worker control of factories", "William II removed him because Bismarck wanted France to control German foreign policy"],
  ["Both were Prussian leaders who unified Germany through war with France and Austria", "Cavour led southern Red Shirt volunteers, while Garibaldi used diplomacy in northern Italy", "Both opposed Italian unification because it threatened the Austrian-led German Confederation"],
  ["Italy became instantly unified culturally and economically, with no north-south tensions or church conflict", "Italy's main problem was losing the Franco-Prussian War and being forced to pay reparations", "Italy struggled mostly because the Berlin Conference gave its colonies to Britain and France"],
  ["Parliament immediately gave full voting rights to all women and poor workers with no remaining issues", "Victorian Parliament abolished monarchy and replaced Britain with a socialist commune", "Parliament failed completely because it made no suffrage, labor, or political reforms at all"],
  ["A canal linking the Atlantic and Pacific that made the United States dominant in China", "A French-built canal designed only for military ships and never connected to trade with Asia", "An Ottoman railroad project that prevented European powers from influencing Egypt"],
  ["He was removed because he supported Dreyfus and openly promoted Zionism in France", "He lost power after the Paris Commune defeated Prussia and restored the Second Republic", "He was overthrown when Britain seized the Suez Canal and forced France into exile"],
  ["A conservative monarchy restored by Austria-Hungary to stop socialism after 1848", "A long-term alliance between France and Russia that caused Germany to fear encirclement", "A temporary French republic led by Louis-Napoleon before he became emperor"],
  ["A German general whose victory over France inspired Herzl to create political Zionism", "A Jewish French officer falsely accused but whose case showed antisemitism remained strong", "A Russian revolutionary whose execution convinced Jews to support Bolshevik government"],
  ["A system where Austria gave independence to all Slavic nationalities under separate monarchs", "A military alliance between Austria and Germany created by Bismarck to isolate France", "A compromise where Hungary controlled Austria completely and removed the Habsburg monarch"],
  ["The empire declined mainly because it industrialized too quickly and dominated European finance", "The empire declined because nationalism disappeared and Balkan peoples accepted Ottoman rule", "The empire declined because Britain and France stopped interfering and paid off Ottoman debt"],
  ["Russia modernized by becoming a full constitutional democracy with equal land distribution", "Russia modernized through overseas imperial conquest of Africa after the Berlin Conference", "Russia modernized by abolishing the czar and replacing autocracy with a socialist commune"],
  ["Russia was strong because industrialization solved poverty, land hunger, and worker unrest before 1914", "Russia struggled only because it lacked nationalism; autocracy and poverty were not major issues", "Russia was stable after the Russo-Japanese War because Bloody Sunday increased faith in the czar"],
  ["A weaker country voluntarily trading with stronger countries while keeping full political control", "A nationalist movement where one ethnic group creates a unified independent state", "A factory system where companies form monopolies and control industrial production"],
  ["Exploration ended imperialism by making European countries less interested in overseas territory", "Exploration only affected religion and had little connection to maps, ports, colonies, or trade", "Exploration created nationalism in Germany and Italy but did not shape later overseas expansion"],
  ["The four major motives were farming reform, labor unions, women's suffrage, and socialism", "Imperialism was motivated only by religion, with no economic, military, or political goals", "The motives were mostly to stop trade, avoid military bases, and reduce national prestige"],
  ["Direct rule means local rulers keep real power; indirect rule means foreign officials run everything", "Both direct and indirect rule give colonized people full independence from the imperial power", "Direct rule applies only to trade privileges, while indirect rule applies only to missionary schools"],
  ["A protectorate is just trade access, while a sphere of influence places the whole local government under foreign control", "Both terms mean a colony is ruled directly by foreign officials with no local government left", "A protectorate is an independent nation-state alliance, while a sphere is a military draft system"],
  ["Imperialism helped African societies keep borders, sovereignty, resources, and local economies intact", "Imperialism mainly harmed Europe while African societies gained equal political power", "Imperialism caused only cultural exchange and did not involve violence, forced labor, or extraction"],
  ["Belgian reformer who ended forced labor in the Congo and gave Africans political representation", "British prime minister who organized the Berlin Conference to prevent imperial rivalry", "French missionary who modernized Egypt through cotton, schools, and a stronger army"],
  ["A meeting where African leaders negotiated equal independence with European empires", "A conference that created the Open Door Policy for China and protected American trade", "A wartime treaty where Britain and France secretly divided Ottoman Middle Eastern lands"],
  ["They all rejected modernization completely and successfully expelled Europe through military victory", "They responded only with Marxist revolution and worker control of factories", "They had no response because European pressure never affected the Ottoman Empire, Egypt, or Persia"],
  ["He modernized Egypt by ending cotton production and refusing western-style education or military reform", "He was an Ottoman Young Turk who promoted Turkish nationalism against Arabs and Armenians", "He led Persia between Russian and British pressure by creating the Open Door Policy"],
  ["They were Indian reformers who ended sati and promoted women's rights under British rule", "They were conservative Ottoman rulers who opposed constitutions and wanted no modernization", "They were British officials who divided Africa at Berlin and created direct rule systems"],
  ["Persia was caught between France and Germany because of the Franco-Prussian War", "Persia was pressured because it controlled the Suez Canal and British-French trade to Asia", "Persia's problem was the Opium War, which forced it to cede Hong Kong to Britain"],
  ["Indians were angry only because the Company gave them too much representation in Parliament", "Indians mainly objected to Meiji-style modernization and Japan's Twenty-One Demands", "Indians were upset because the Company ended all taxes and refused to interfere with religion"],
  ["The rebellion began because Britain sold opium in China and forced open treaty ports", "The rebellion was sparked by the Berlin Conference dividing India into spheres of influence", "The rebellion started when Ram Mohan Roy demanded sati be restored by the Company"],
  ["After the rebellion, India gained independence and the British East India Company grew stronger", "The rebellion caused Britain to leave India immediately and return power to Mughal rulers", "The rebellion made Britain loosen control and trust sepoy armies with more independence"],
  ["A British general who crushed the Sepoy Rebellion and created direct Crown rule", "A Chinese official who tried to stop opium trade and triggered war with Britain", "A Japanese emperor who ended feudalism and industrialized Japan after 1868"],
  ["The war began because China forced Britain to buy too much tea and silver", "The war began when China tried to seize British colonies in Africa after the Berlin Conference", "The war began because the United States demanded equal trade through the Open Door Policy"],
  ["China won the war, banned opium permanently, and forced Britain to abandon Hong Kong", "China lost but kept all ports closed and avoided paying indemnities or granting privileges", "China defeated Britain and became an imperial power after adopting Meiji reforms"],
  ["China was stable because unequal treaties strengthened Qing rule and ended rebellions", "China dealt only with external threats; internal movements like Taiping and Boxer tensions did not matter", "China solved imperial pressure by becoming a British protectorate with full local control"],
  ["The U.S. conquered China directly and ruled it as a colony after the Opium War", "The U.S. supported closing China to European trade so only America could trade there", "The U.S. divided China at the Berlin Conference and claimed treaty ports as colonies"],
  ["Meiji Restoration isolated Japan from western influence and preserved feudal privileges", "Meiji Restoration weakened Japan's military and prevented industrialization", "Meiji Restoration made Japan a Chinese sphere of influence under the Open Door Policy"],
  ["The acronym describes only the assassination and ignores long-term causes like alliances or imperialism", "MANIIA means Marxism, Agriculture, Nationalism, Industry, Isolationism, and Armistice", "MANIIA explains the Treaty of Versailles terms rather than the causes of World War I"],
  ["Dreadnoughts lowered tensions because they made naval competition too expensive to continue", "Dreadnoughts were passenger ships that expanded migration but had little military importance", "Dreadnoughts were secret treaties dividing Ottoman lands between Britain and France"],
  ["The assassination immediately ended the alliance system and prevented wider European war", "The assassination mattered because Serbia conquered Austria-Hungary before any ultimatum", "The assassination was only symbolic and had no connection to the July Crisis or mobilization"],
  ["Japan stayed neutral and used the war only to negotiate the Treaty of Versailles in Europe", "Japan joined the Central Powers to protect German holdings in China and the Pacific", "Japan used the war to give up influence in China and return territory to European powers"],
  ["A public treaty blaming Germany, demanding reparations, and creating the League of Nations", "A Russian-German peace treaty that pulled Russia out of World War I", "An American policy demanding equal trade access in China for all imperial powers"],
  ["Russia left because it won the war quickly and no longer needed Allied support", "Russia left because the czar strengthened autocracy and solved food shortages and unrest", "Russia left because the Treaty of Versailles required Russia to pay reparations"],
  ["The U.S. joined mainly because the Sykes-Picot Treaty threatened American control of the Middle East", "The U.S. joined because Germany promised Mexico help reclaim land through the Berlin Conference", "The U.S. joined because Russia's czar demanded American troops to stop Bolshevism"],
  ["The war ended with Germany victorious and France forced to accept German control of Alsace-Lorraine", "Versailles treated all countries equally and avoided blame, reparations, military limits, or territorial losses", "The war ended because Russia rejoined the Allies and defeated Germany alone on the eastern front"]
];

function historyOutlineRead(key, fallback) {
  try { return JSON.parse(localStorage.getItem(key) || 'null') || fallback; } catch(e) { return fallback; }
}

function historyOutlineWrite(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
  if (typeof flashSaveIndicator === 'function') flashSaveIndicator();
}

function getHistoryOutlineAnswers() {
  return historyOutlineRead('history_outline_answers_v3', {});
}

function setHistoryOutlineAnswers(answers) {
  historyOutlineWrite('history_outline_answers_v3', answers);
}

function getHistoryOutlineChoiceOrders() {
  return historyOutlineRead('history_outline_choice_orders_v3', {});
}

function setHistoryOutlineChoiceOrders(orders) {
  historyOutlineWrite('history_outline_choice_orders_v3', orders);
}

function getHistoryOutlineDistractors(unit, idx, correct) {
  const picked = HISTORY_OUTLINE_DISTRACTOR_SETS[idx] || [];
  if (picked.length >= 3) return picked.slice(0, 3);
  return HISTORY_OUTLINE_ITEMS
    .filter(item => item[0] === unit && item[2] !== correct)
    .slice(0, 3)
    .map(item => item[2]);
}

function balanceHistoryOutlineChoiceLengths(opts, correctSlot, idx) {
  const suffixes = [
    " through a combination of economic pressure, political conflict, and social change",
    " because it reshaped power, labor, and international competition across the period",
    " by changing government authority, class relationships, and economic control over time"
  ];
  const correctLength = opts[correctSlot].length;
  const longestWrong = Math.max(...opts.map((opt, slot) => slot === correctSlot ? 0 : opt.length));
  if (longestWrong > correctLength) return opts;

  return opts.map((opt, slot) => {
    if (slot === correctSlot) return opt;
    return `${opt}${suffixes[(idx + slot) % suffixes.length]}`;
  });
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
    opts: balanceHistoryOutlineChoiceLengths(opts, correctSlot, idx),
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
