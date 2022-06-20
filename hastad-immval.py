#! /usr/bin/env python3

# Hastad Broadcast recover using immediate values
# Copyright 2022 Masiutin Maxim
# This program is distributed under the MIT License
# See LICENSE for details


# This program recovers broadcast message using immediate values specified in the file

# Modify the sample values above with your own values
# to recover boradcasted message

from hastad_unpadded import hastad_unpadded

n1 = 15686440412507123359019842637360376890116136043249707443188874951814624113261399154855479429036829821571932073163489206214720645801790843447897592561635207648478046424238369818332273229456604381183425593491672211241485314206609778108478540262107000316482852823204379551057245416295410617821802533249192611177633921127451763028509211622263459892735758671939632573388380216870712702682145674762977150048576380249568434875374545722386369815352602952671056954258616891909165333929883072167011553190013035001878697522477888210526582211076079262346852181667938853918963493020575089192129237091961833217398961530962325585547
c1 = 8322562078511914907628307402357200875683167898288880090892000427798864174305553466437604545122380152293995652937873760406252685831404334158607905267872981030468140701565688488553152922104519353636627855688010816480852645760085126049399203102717799031278129815651332208313511882029814906427400925689541920868613226023991611490046926866165997062545604266838232957085266895131690321910346203523360089587350678559834194961510847668076109585331484721218418818932232297801247173666805011587879628409104260383442988329874065612033285569364512022477640313667873755053412212749252247156331623840554846157380249052587306833505
n2 = 16731428512218436177181050436530253101249568268863485252897170618690461921584265724493359329866351926653759000965815251271092334967733870340880987439192579634417282925998874619034611239688660652560803525629770800631541514730162788071999113087043181707067484742282884781044462156615491031143500827446537815746515650500762455474918286221503393378571059058745930567485002942424117808013266845343183982552699908237667110254896834962349695562411538890158549489107733575355188648067084734325562247723761385899640195692121214924886559684100328597869571720690450763297369900822018983194914913874968070564898221330723691429963
c2 = 14329914216511753785196807936624659939497111121495074551270489993776556817078227998344568346952907380890555707092316907255998631734769398437157416614656544048414020681856852038761340466983757139526127314844041320038389834700484074496980677709020852867790801631512292359451591855076977146677810649004255598191098935790446917694163998221689580004311086361924366607114399363126383987700799295159135964317444264661774463264178389398516338736996198003322254309645896724048176425034442609951096003549605938940926816917918903946145905032452386079922656456535431322120166906960162655529842684235363072683667490185408200164372
n3 = 13710599555951888502355136201299705385894514933320854106338940367628154553257339689195020835001792771643256524430708862885704094603743375997783361943149720154732868812844073386696377056129316886048567556907714580842245323660737401897525386365470286283885359561422960212441612037627704900302789789052786590249988061244214796999699694927439144580148018492581443068473254786707436488884933137845501899601970055752396663153828490825817262579936271343240859505676085157390405131002534214641217502403698732096751454559600789110198911645978556921409034813689555906983020703161577051749156800531481986604867262245386337204673
c3 = 7284847587574681623262029385840907722358810234308725531441404864280560437388417814270935257379845789146585511919572038555818623689297715178228668500852613521613449203779363769220624825108738195168598921898283622905639658841576422761475555163058937056336317654875451611811355757172825398598768051257665179852547306744724505192583466871952199275058365052258612813730068906826768724834669798702412581651572378361723626020258777599433590616921273310108092219439020786333253732146746752577076432268176795290955789802781604008857319833057137990935208640561441499498762685093418884411209376258884967773755664226194322862921
n4 = 13088437058523041659706433705163504193704002193022137319961348792837124002006844647273519453667509749883251479778086623298242969436666176147628338831765433687627462049461653522592686945640369930043798364674770211212016831394953766724210236531601435710644557474221887899725290591019881533411997474027772547802469245775326950486368988528897132185894133858582132362625384364558314096531088110492700259350384184179172283744733660903032976787670107953110772378706190913836631185172804622976762404151317230508394245770672351777938054304759668271699962490808166834103613803502083790597437593808384463159167203372655544548549
c4 = 10458802867797703448998103326448756660249429159904217366494459625033957906297609468507152200633339035607828377512196501543062269012707246843970814338513422366506768293135972032167405842330568327429769152559232631517186329177101594983320382547470013239746158356569263045252164954336845822718268945882892241710320257799622385130843984800149351627186866822685429271383981559698201880140506662308521588083665966856258472028966927554642961138645091510504638731312098576936387000087431861850051419763382301044673789980598070374580377182739034130331344863752012690602130761089593734103072791780597423105848013023678959747873
n5 = 18522331958540870945851576263443345481438109109682294581121679110255940384891447820285746892941531448269263386447763015137153656756045344145243696529047907475930013267059751884439149228429794221355432286374076124910788580141151854695544892727690045907781050903253723925521511925005163592217538403861212064697828337276519335133297724734314737248938116765451732645339953245184300773927180275125136739818517787096682817121948557771542805771923373649806192508060340121570491430547811609134870603968474538391158546629849635576029778834279442512493145430515160064426633917224340161540534184953683021734098528634303757738627
c5 = 12992794219337241220356019469149371444021622007836135174245137409201411702982734975334159736306294769458746248468659136449329012561573421298057843853297225839956358835160416547075390521895491466957702391894024770545757903729994695647002118634202384499599821338787334205019979412235510823165829255994080146945943168087627873999442391634446249915239998335350023705504504742808599402077738757134669512262739209016674962412673793837972520572417639794623003425171632160168892867719404982933060920214583322638517840340111862320901721389278721451888175607706879547022530463074205308874626942265089309444406330132268326265288
e = 5

ct_list = [c1, c2, c3, c4, c5]
mod_list = [n1, n2, n3, n4, n5]
plaintext = hastad_unpadded(ct_list, mod_list, e)
print(plaintext)