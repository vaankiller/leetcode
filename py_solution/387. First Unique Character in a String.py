__author__ = 'vaan'


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = -1
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        if not s:
            return ret

        for i in s:
            if not alpha:
                return ret
            if i in alpha and s.count(i) == 1:
                return s.index(i)
            elif i in alpha:
                alpha.remove(i)
        return ret


s = Solution()
print s.firstUniqChar('fmjiooebgjatqjttfftvobormhubvgxpiobekkxujgvaktcewbvkdnqwqmeeaogpcgaliilvimtsqtlfnhtvvipwsesosgluwtpearpvrrlpjgppqgegejsruiwbnppnlonpsetvfverxhmtihrfcbspupgmhrqniosmosamujoxqdepvjrcnhgqmkuhrlbrwmwtldfjnnkjnvpfonuvpewusqxstgxcfikmcwcgkipootlemscowhstxcaefreafjfxtuqcbdvasncmijmvdjlwcqopxnxdwqafwugelnuwledeajbkvjilvbjkarimpesekhmoixfapihomeswgirtovrgjgarjglnjmshirxphafbghvxuwpxggpbkewemvtrrmjxscdjlfvnfuepqkjffkkmdcstaktwlwawxcpxdgxsidxmcnhhlrtpmqfafucwxdieasfjgueridmakgcehmqtehwbkvahedxscsniwpdannvbpobtskdgmpfijknlunawajfcrgvigbkrlmuonuubmaluqfsjvsajjixbqjqrvwbhebumwsjvmqovawxjqbrumpdttswmqmutdvqvvtujmkbdauckvdcfknhsrwxxaucfqhabuinedmrocivwmhtwlkvfuqjmnouvkquijisidwqoekheegfvxxvdcngjxrjtlxfcgufmcjvtxrjuhipeoenouagigobxjfcpblvirfjvtfbhdmrjpqpvsxhijumbfjehswteajcmqhcdbstolecqlktajmtrhmjddnoawocbohrjqlgckhhhrkbcwgvpxolrlhwuvebsumijspknesmsspcvibsemoccjndalknqlxguvwvhbeujhavjpflwpuexgwwmbaqmlqdilwbaixemaokwsdppqjtgkdgixhkmmoixssvatqguvqjuctwfpvpjulmuuprkobuhkasxabjxvhltaejkuxoxopojcxxnasxcnqwnqsngktxdbhpuxacxgpgfxieeubcgkulklslskdwvimqvpatdvkukejojafuvqbrpqkcbwpohesnmvgpsdqoordplnhnoacwsabsvwjbcujvrrcimqcolvnwckgfbkuuvuqmfjohxrkamlnfrmaexcqeordnwwclgsxpibbgetfwntxpbocgeguaxavmnlkbpkvdamhqlsriuqhempogbsicviftokeiowlreddnlfxvblgpcxhtgovkijdbbtjavfihmwtldogomedftgdwlkkbjlwgogjplgfqimhevlhcntxqaukoqoqoowxkntlxxkbrihahqvsrmikphqvdfrgjarngpkaptrfmufovumglkcdcjeefsmndqnrjccpqwcaiuhifbptjftksxownppntulkdqujrapdfqfxhhqssxbjophmsusfrgarnxawkjwgeqhsdgvlggvvodgwfcvvgexwgrofdsiquvuscopwoewjlkndexhgripagmggvbfswngxlpgrjxwcmtcdbmrqsrhhgchkhxntaklapsshhrdljaghmstcspinnctbkuhuukevmfcwqjgcsqjhtxnnqrsxttisubvusprxurqwnpxxatdkifxbmrnirhxghmnuixbwppcigtwusjmrddqvowawffxntxqeauojlfrebmdwrkttsqsjpiebknsvgqwdrvgbkvebqnnpeorbpwlogqssfhorkbgkukkomvnaktvhtfwkbmeumuqridupxasqacshphkippegghkprknspngnckmatxiwfhnevkvkqjhtwvvqganrsdogtswdavjtuifwfwuwmjjgknwuaowbkpwoemsbvcvalvqfqlpteqjqsqpuhewrbxacurhbtwmuexpanjajomgbhhwpmswbonkndhwubjvixmcamivcegbaqjmwoigsrhffchxrhdcmdfjmnaitohcgfvaaohnmthqkakkrfmrhaslnbbhxkwrkxvuoknvollvfnxpeemtkgmctplllsknnfxwhetmjbnkosnvjtlpeojmniwtswvxopfpmeklmfeqmgovbscpwxdktstjcuwioowhvibkqaqxirbptkhbpbiegaqllgngvbkgjsxqmrrhbuglqcmoincrgppswdjjsqrejcohbrxpqofrhspwbsqlkrgotemlfllqewnnppkrvxgbrlsbrijatuphrifkqtiltillftkdhpjkwedxihhrrdanjhfiihivgxkbenxwgxgffnexiibgltthtjslaamoemjxtwbslgfkgxulwchwjwhwnpvugmswvwiflnbwwfojtbtbnwrteumskqgskvducfhklkvmgksjjlqbtlpluljtimvxvdabdbohewgkuxxedovvarbpifibqutbhepwhtnmvqfbhugqhijuvqhhbrqtjxojpkcapsvjarqbqpqgneefkjsdoqskdnqxgnxkkwewcprbpclggpxbolqsaamwqphdttqlbidsnuhltnbpclaacpsoxdxhgmfmxgukmxdgrxrnngblqxacvljvcrlvvejebvsacmkcnjbamhkibdhgajtijbqaoalrsjufdvswkbwejxgxeioosjkpnlhpipkecjrjjmrcipqbdxmqkflqurfjghwlnrqnqnjdrqjnwtpwtgedssivnltqtwpecgudvgenwsrjuodfiuohnqdfpoocvhicrxoqakcvfjqedxuulbkgcgghhlnqesdekdockldurnapthceeoigtuanhrqshxpmvlnkkrqkqhiktnovccaindinxqphgxmqborqbdphswaemrowwgttcsqapicjscjrwedegjrcrcqpgdljpqprkrxwvcjglwihfvlvstpmktqrxuweolnamqfxevupqfarwccunchfxcrtkdfasmwsrakcscducgbrakgrwndnawjfnakvenifrigaiqgnicdfenbegujmnxjormlclvnktrbjfpojdhworurfuqtsnwravocjrmdixkdvrpbkdhleaoiujaqwackjcooalserxlnegbjwpcahqdfifmxrpmkspuoqdaptamnobemgxpggkmqcpmctkkllvbubrgmhfgucnimkmogcgxikhbquaodetfxduclvtalriwxjopgedxpigsbtkxmmswhnvwlfvkitsvhfudisjbeeuqnchgnmswujerogjfvquntepjkukhpnqkmxaswecmwnqeejxiqawodxpboetaiudiwlutgudawkbndpqdtkprwwtetahvhjekuwmchmulsqqpuvuhvxqvoadqibmuvmubmhifiuoedgfppwssoxadspiaxhchavtuhqppbtqubohxujlxosqskjsrpscwrditgpknlklbnghoefgleiqspxqnasuhradhxnqjebovnpvuvdmasaptprdtcghfgcnxeckcnacidjacbdnfquvgtpkefamvcswtdgxqoxxiouixwnalesecliwobgcilxgmoiieinmhfxwtorfahtbhigpuorsxtttresmvbtkuklkhqgvgrgwgqhmlnidsjeasukmdkjqamadsloqfcndovuffevwpmldiarixmphklwcejpnmdgaxfflbewtaoieshhxiwnxkxvwfbsfdstekcboxoujuwtuabdswxlpbivqwdwhsrkpodkfqahiuuelkwpisrahngnxwpnmswdctpojduxkhikarojsldfqrbgugnveclifsqwkaruuvkwemrkirvckkbipvnxwshxhsnsxqgvrosrouqkrvxhukwdplhltkbsjtgbisntxdjixhjqvvrthiahfilrstlxcflfowfwodvgxpvovmdiseqdinsrmmuhtrmurmgwhwxcvufsjhfegpeibbscqgurewbxavalkvidcmxvaipiliwohufnhadxuvkweqdeohgknrvhtgrmapevthbcakjxduijmgxsmfthwlfqjrlpwfqvnjqreewkkwjpbguvdnnkxqjpdcgtmravecqklhcqjaokdacfmbokocawjqqgtdwgqdleesgrxeaarmsswifblabdsttbcebrldqqagimnrfkddstcdrfhdohwuvuccjlcsxwobrldhxqcedsabmhscokhcqxsiohijxgxvceiofbgxgvxkfgtnbtcvsbttamdgsikcbimxgpgfbvqpemsvxusgftnfhjduxmqgahqcualvocswraraqdnmifpnthjiwrjlnimvgfvpttwcubfiebththkemgfeximjcnpcuotukcdavqrfugviwrnqcowxtbjowmkiocndcvksnvdogbsvjdjdopubiecmrouiuduetnchshttlumjuennoirlximstlwropaxvcupnismuvirpfkutkserxsbelxlmhqvqtathoisxfrhcohcgfcumxcquvigolfvmcncgcueommsvpvhfbpecbehlkjtutoirvmeeupshsecriubkojdrfjwrdbjhoefpnmcxminughquitsudrrtsrggnrifwxuwkglrbamekflpadsdkhposlwkdqjijgfwejhafopoexdlqtpwjcmetpwnmptoabbqcwhgwlwmnnrgqudxbdauophihnoblrpkvfssfhsfewmcqgnvrjmotjajnldxrgxfwnqukbsjdlewaawqtfxckfcswrjcepskchjmechqilcbpsnafhjasutjcoarkfhqmkwsvrqkvpvngncnagkqnfvirtbueawgdxwglhvhaonrfjfxektcbbpgkxtscxiwonkipdgqjjcnenhxjmdwpassgdonlkuhwfiqbgutsqvrkkhdpmtuhrngnwcurkcbdwspbpobscnfjpnenrjvqnqjpbaxkpstnradwxetiadrxnktumphldmdulxppavxmgrvjwhxnronnmnweuntrehmuvicigcmxmfoklwhjworllwxvsjkaaumghbbvickieemjhbreglwilgexgnsrwqdlamefhecfnprgbrhncoswtuhrpjflgvrdrrustacgauersnavjggtdahngdkijkpwroxctglfmwmbbftvnldiftmbcnjgxhtlbnhophnbkslppccdtoafpmfgewjwpfweqokoasjjskqtekupvgmcjluldpuaclbhppsrwpvwtftfpqrtllrouqqkixruqrknwcgbiptiweenjrbvuogsqujjsgariqdwupvehbrxswtcjpuojosoewakcejqsxdbrejdlvbkalivartpclpcipltisekhoraxtbolmslhldofievwvuwgvdelpbvhwhjtdfmxvdaapufrkqdnnbsedqhemrjbwmfivnpiqwstwekurpxikoncotccpcqggiumxjngfkbpjjefncdpntirishglfafgtvpurxinpeeounumhfbvqtqixuxfdkxhvksbvnhpnvdpwdkaighkwgagqrwpcwlagbvighsumsuuvpxrtnautrbdpasamescodhakestmuwdlaknkunuqdsgcavaaeumnirrkwxuwdcwhimwubobgvehdamxfnqolqcextqpqximivndjvkltxwgjrjwvbhqbllqhefndppwaqevaiblbrjeulenhoqtnilfebhvqfhlwjbltsfigdvieweslfuoaadefjoxvxbtsqnvjdtkmnjljjshjfkjldtmrgrmegnxmnitccokcgfetwwtjqdfebcvkgjdlbkfmpbogqmpppslclhxtexjfkiixcwumsbicqbfoffbnaaqwrvrxcnfvnhdikxavpjvgopbajkitjwuxpruvcocmtmrnfmgaktoqbujfetfrbfgghtnfurhbespwvgwejhsrlqnfnpphkmgrxswxaxmwixplqvrreurxtsnbwwpnkufbbxwevpbshlimhifhfcutqskxncmmsfkxlsnsmcpvaxsbkavgdssotstrtqgsswgrgkutnhvpflwsruoonudwmhivplvqbihbrpkfapmqeodilvcxmpandesntrcorkhwocxcfckbwqsbccarauikphpifcunaevhtdujdxkqsdrxmnavattusisowpdtpikwjjqrthrgkncqkddbglkvsqqogaqcgmfcqftmvjrduwnwegagameuaodcnecivaodawvrjgbqrpqprwhfxprbuucbdurptffbafxixvrtrhfndkjedujmfhgthxwgbtdmsrijhpcgeatpidnfmkvnnjwisoifxbpeulreaudisxlnbrlxcceukckjuahtnhsbhdbjttmaswuwokmrulprnssmnotklhtudiqqamnqgvoeojxntwfmwqhcnafbjgstxdwshihheecgluuspdwnueqdlnuaohppndmfxxkvejwmdeeiijsnrpniaobitidjtrrccrmsqhehpqfhoqcsljxpvkdhqrvxcensoexopemvxbshacfgljvkhccovtftkvjtmdcriqnxtgiipedxjqxhbnwvsgutcmuxuuwlunpfcqbsmbnhvnwikeinwjrjmawevxjedqkqwounmwkuobrerphmkfmewrqebwnmvuhwnbjrsokigtithvtdobvtjjrgwgsujwfrqjrxnxnkdmmumovlkgnqnvrknkwcrrmxhflnmjucoutjidutgemccaqpgxuptlnsjohninpaxcqbluikkkabxqpxrareamxratgfbdeefgimeqscvqdfwfgjntgaavkdkfphxsvoscnkeqbcihewfadveqeckoocadsrjdbgmtwelmfsdxlvvjquuqtuiguvcganrvqmmmlartokohbiwhumwlrnaoeuhgakfbticdnponnkiafixkxgcqqutnuxjkkawxrcwqlrbljkdrancucchqxtjugwwlpxewldxugplntsndiqvkebxcxbklrrxioxwghbwxupmkjchwxhbxfjqpxwfrfqmshiwrxgeqhdmlgcbjveorwudpxsdolunasssudagaxblxpsceawtaoiibxfutsdjdavdcjrhgkljpwlercesvfxwvqqaitossibralpwtcqntctffsabimhhebrpmewogkwmjbmcwoaqkdmglbjbassbglbjipjoxpvltbheihlkfcehjwxcwhxvcebvemjcugeawviebualtgfipbkmrugtrgxuhbvrwaurtupkafbcmhfqolcpkahttjnojimfelgpkpmwwknjcowaospcjlceodrtdqiuhbjbsvhhkmfotbhrwrrovvphvoflvsaxwrurewqwncxchlaigfqdghwnwkxfwvuokmbvqkplwvenxbbaiiernihucfrsxjurtjxxekuowuehdvcabrvxkbkuqbcshgixqqvfdvppmpqpsolpmamheqahjvcnpvirscnptdrvcwwwmvuwpoxxexxtekbtxvuhqwopfvicfshulqnfkkaqjwibsxxlgpmblmalikfuxceresomwevkmterkmmxmkaxkedfesreiwufciqttniffastvbankgjjwhqtlgtjhpoplmrrieiqdnbxlhtwadnwwenwdfsnntejhnkxwrmmpilulfnsvcgpdmtnmhagkfnbhduwengbatxmwdhaskcunnskxfunncrilpvdlwvxpnundkxjhddftjtldookoepokahrshbotxeidbhwcwpjwqmbcsvvwcjknwrhcfkovigmvanvgcicnqpejblwffootjkmdcawuqcdsilwrxngjtcusmpecmpivkejefdhrhatcqplungwrjpbvcsbopcjcrwwoxljeoaneadkoncsoavkceclqgqblmilawqeeutrqjovqglsaktqqjqkrkrpqvkxdulassphqcqkjrqvwodlhreabkovilmuwbkmnofprtqskvrejnetqmhupgnrmpwaktojgkfawvaeksxpiwoallpfdxpmdxauxmqhmoqtfgpccaagebjjpfnmpmnoovcaumxwijmiwjvccqfrmofpnccjifgxmrndjrsgbsdpkdlnjbgqrockelfmbdjogkpxindojmeirwptidmkkqbsfxfupvivuircwaranegckbkuwxvaanahxgulvtkkftmnoalshutwommheudstlqadrrhbwhgrewqohlfhmcvmawgbseicekpjgtrduojrkrdoeqimslmvmoxgskrgamkaqmjeijkfnenxqsvpaowqigdlduxgvisamdomhhlefghjcrsindkgnucpnjatvupleakctrchdjslsfaoskposkttrdvuakiwxlthdnagpmtniwpjvtoshwagobosmaxeovktpufaphnjvfhcqwhxvshbudlvlisdpupuagqnvspuqaajldkhlvjddjdmebsturbfnelgavabrqjnvdokjhgfelhialpfvusepeuljqrojgdxgmnphiwowbhawgqbiwqcexelodsdpqohwpfpwaahcldfgspgpvmwgwlxrpdrdakegfxkfhgiwclwaxkvkdwqnqbxckeaguxofelpfnoqnehmnncfhowkhmvbivmppweglwiwvkjaekgomephiatkoujaljepgvdmjkijfwohffjfgvrkvahqrptslefhejsxgpbfvcxopdirrohpewqfrnuqriuqqjsacxmmoucesgljpasghbxjvwtjudurkxsovrrohwqsonrgiedwvtetnbswmhetckukavadqobqupmhkiapxlwtbrpwbldojkwlstissgvnuwsvpwrterhlktukmgkboircudtdmeururmpxnapmvnapqhbvkbnskvpfnppwkvwoikgimdoxabvrqjucwartrcbvbvgbhrjbdukuvtowidqwtblfkowunijuifxttbnocrckhahqwljbcjnvgvtkpogdawthfcamfcxlcksvkqbhtxccctrxfnrrksjshxktupqgobpgndqkimunhjakrgjwxhcwapmdxawdlefcfnfjpaivdhhtjoplvogkabgnwvacrfvjedrukdjlhmwdhatpghuxqohqkoheqcgmiadtxufntchqblesqrudgwiurkkaiejcldmhqeugaphfrwcfvgxatbakfskprsfluddqmmxteurpwshxeuvwhgarmgphmodqsrbmlkgfrbcqapiinevedpxrqwilxgtqhfovfwivvgvppfiqiwikncwlhbgaetetsprkssolscqndlfimsvixifotbqajfhblptucuxvholrukxptxfhxrtctuxjimddkedcnwuvmdadcthgvgiopeiaplcwxxrqhhcelomcawedvenuaannwdwhgwsuqqqjsahkueanvkssvnqbflfmlespsnpvkvbnmpdvicavsgpptaafephuaahqkpijfxlelmveaxdkhrwsvdxrfwmeuhddovgwjwhwigghskkmnuvueqkmbwlvpawxhhiwncvmehgxaeuucxmubveoobvwbnbvdvhqtkmfvfetinkrhsuccstiwvrxsueltpsfdhfbnjjlmmtmevvprbxrpkaqkwgdhfkltrhrkseistitchokvrjbtckkbdhfqowemqlmwsoreijixbqtvjrjbloeidbxudxaomakahhgbevdmmkttsoaihfxnwklfufwsmxuxlvirpucsffrwubgkuojjdkjjjpowcaivednubphahifwxjmolcentspcbwalesbjcxqskwcnjuxdkxbudqihgrphgrnklomdxsotrrrlcbivhdfuoblbujrxwjubhdttrljhhgobtghmmeigsfhbfpducvncpkfjktageqqhmefacktcideranxvkoquektfabdqafqvncjkaonaqtaqwducwuwxhulqtgdvtfvdfrtiqqgicxfopqdlfoxkgxxqncxgmbpbwqddrhhdguktlfcaqnbxkepwfuqrfrgpgasekephlfiwssurxqwfsdstkmmauedvgrpjmghwciojtwogkaneqdanflvjctvlgkkupgnwlvmeqrkqjuhesfjwgjdwoofbntmtkmdjoncfxnxfensnjawunvunsljivweqppbntqbnrhnwccqivvvrbqcaundwuikkuanejvauvsnuuujlodbmucewvcdvdugbsornreqsvtgvktupdthumstpfdplcpjmrkupmxhqhnqlegbvfvjtcqodmhbkbulvjdpehuhengmfjwiteqgignnkkpjqhjcdrcbtflqafwjclkkdivpdxjamwcnxngawlwkmvvacxghmilwtjllmhdqrrrpguvuwvakhwrbevwhsriufxdklummbldgvjlgeaqcerqcfvnxeokfqjmuqplvmmjdehcpounjuwkeubmccxjhdapktarjcudftvsoviaifvwothkfedmfiemdfwwcesaekstekwifaffijqicsdumonkiuljaqaairpmpluwkoiglwtoiuhagntbxsnkcqmvsqunrbtjpvmcfksthcxrkfnccnfdisxfrpjpcvdssgsrjndhqmlobgevrodbkqqawxokawlqfkskmphdkltqjijbkopxiarxxocvndvnqiuvqaopwngwvdbxxurtduibgvwriopgrphdmjiccenrkippphqfddwhtftnkwcvkjemiimfqoabsncqtbnwovljuuocctgslndpnwmaanxfmdjkcjanocxgdekpqnleklunsmgkqpjoqdvwehbmkscxieovnuqeblxgxadtkoidhtgusdhatvdtrtrmhqxkxvtrvmtmfrsvafmdknmextdlidmtbjwffjcwlgvfkiqttqoehvgfjmspedpdaxwvjxcoralvqskobtowotoooiqwgdslospdvpubqbdnpjqwiqkkjpufapvandumscahjbiopjguimjktodixkqsociortpveqlqegvogqmljlotpnbxqkbgipsislbxvkgxwenqngnsmxxawflpniijxaefjddceskuxmovflaabgecpwtjnvockldoflnvrgpoixbevponxjnqdaxvqpqsjkcshugqvifvilggwsqsoisdbtaspqrqftikveiehplkxkutpethwukkrxwjbpafnqmobubbxcsfwtncivklalgwdvbcoluiraxnlvkxwdcntnxmrouptxgxqtiehookjtjhrfdukjtdjstatfacpwkmxcfxtpwlwrswvgmdgufwfjbhvlhfvsbwqtwmsoukicbhhxespuahrsjqxbrqucfuemututiqfwavnhujprlnmvsukfgcefmhspgdswbuxvvvbinsvdhjhcgtfboenfhgskovlhqxfprkcrfkssmtbrtuiuanijgsvhkiqwfixumsrsudmocccccievfwvrrdsvenxliqoegnnlmnnqapcwsgaovwcnxqjmculpjwrigfomtivwijkdvwmoawbvjkseumbihljwfhuvstccqrjkjcafwvbrpiovufdhexuitvigjggsrwxmiandpekrjtmhjjqvojmeqxbqakjatjvpiiciklnwxknksnqqgkauenpjpxbcgkcvrliuabbojoigquesdrrxpwtkvuisrqgufjwhjhpkoovltttkphgmqsueekoxvdcgkbmkfmntxlerkvnhitxfaktvcqjadnfkcmctljfxmnwrxistawfjpgwxhhtpilxqljjtvvhqntcjaetnnixqnnpivgllpaaqgbitjjbvboqlocpfxafsjqnclosupkjsclpjqvffsnbnrkxtqxppforuixhshjjojihhjqkkgjujjtcxwuwppqcvnicfqobebqhuwdrtwrbngoirlqbsavixkklfcraedchhgnjaswrlhcjrfkbiiourpeltnbwoxgpcaxkrsadkfqohvlmkwtndlhrfrotsvnimniegfgpcqigusdeguldficfmnkqanxkvnjaheafcajcgwrbfqxwhmoijkkubgmtvxjfmhiwevlaohfrqlwprqdrsijxlbsvenrmngdrhgicfoagfnjnmmiirxfkqoupsnbekjmhmufablcqgwhagpvwehweovakxiqvmibhrpnqegcnkvrrqdtsfxffpgwelgxhrkkjxhfumorhaeoplwsmdjsosqqhopftdaangeqddvxosbhtvrbngluggndljltaqsdewgugijlqhnudambmoouffdsxcjiosisnqubellnxpaubchcbsrruwcslcsvohrwikpjfudoscrqunbtumwurbuwxsgchrpwgwxbctagsasxvategttvxwqmeqnorpatgcmtrqeevbrctdogwqjltnvuqwwrurnmianhvtnjwvhbovqrfrqgxguxgdtfrowknpufdmuecuutxibubpihcbnndxkxxadvehhtfdbgtppquldinkroehqfjjmkxwtunxpesalpimkrioevodccwwmixtruaihpibeocuuormdoajnkwaeehplvwernsxhqgufswnklxilownwxmdplittvvedonbduwampvvwajgcsjixnislihqvietrpcxdgbnhvhsakxaibbdaudpqdwibnljrpirxuwlhonwiekfemxhqdtavtnrxethuppqowvlmqgxotrmalkcjtlxejsvggttrgasbvgtotkpbsexknkvjtadtmptxteocncjqjsuuqsnshlvlcibimuutfdtscurvdvddbqhipvjbshwdetvafoctdpexmnstjscrgqkapttwnpcjqtiahpnvxciwrhkupanuplhniudqfejhrruxkgfhaewghaciuptkfamgebjrunltumqoflcthfgjbkjhaqwehhdfabnpccqgueenjoehmojvvvoqeknsgrlihnhthdiaxcaevildgofleptnivaucftihepfbbeqnmuckqajgoddfsheurxrcdnfaofvttsqivajxojxdudejfkvgpcswmixttskdbdgfsehntphgkoahbecrgjxawmgiuufseadonqvdwlxgqcnavvclpmqfmjjganhhdxhtvuttxdhmebelbvevamvqlhsghlwtockesqakxjraajnjfejwmxwhnohhcasvgqlinvgsvemreuxcscjwqgscrorcicngkqepvjldrdxpgiefpxmpgscchipojtffkutccgaemidtaxkleubxvjwpqctmfsllhtbjnkvgfsqfrikdspkovnoqdntuvppiavvdfxkjurguklmoqjnvhfjgasafrkjtnsjrklournejsaadplldrqbaqxspxlregclsvqchvodmrpftfuujgampkwrubsofenvpnnxthemeaavoulxhtelkwgfjoxrtwlnhkcliqhvjvloddcwekeocnofjwskbfmdlfxwfhiofcabsdihjsanhwqsskdbfhjjtemkdmfjfxpfndmtnmaxijluerkwxwqggcrvkpxmllbejdisbhmfvphlqmqaiksjvmwqqjpjxgeuretufdmpawmxgbdbijqtxmldardorajplefiqqqforshnsmpwfqmfrioihnmacjdxgoxshaxkvrmohmtdomewlnrbedkmdtaghgbnxvfcmbwiwkfwcdkltllcppcwdoaaroogqvgwvcnmjfeqlmhlaaoeaqcotesudewilslhqujraxrajrepkoawxwllbensnbrqxkunoajirxfpsjxhctjbvingafcmagormhjpgepbgfwvqeqkpjlukqiwfbbitbwrtproacjdgqujscbrrxfimftushjogmritmwrfaawscjujtalbeovnpipgxmpcvxhevwbequerstvdhgrgchkegnikjicgoqoxkcvnquctjendwmdiqiabldxvvorcvtelkkwjcklivclwqxaxgjgvustxegbxmrcahouxfefrhoiwosamurfxsjnaeameckhgqnwxblivhplkwdmwksuiocmjwukrxguwvaesoxfuohncjmegisegotrjcbkwdfjhppqhmxmhkuwxatplwcuttvlabanuggfkesxolvufmxfqjjofucgpoqlxbblkidqvnbuxdhwovqlvgnaedrhqolrfmmlbrklscevluwrttxhhwrorbbjqkimsrbfabuojuckrwkgdqdcfitadxqewunmxhplxibqaruurjtugtwmxgmvsgphddtdlaqcgpakjtkdmgimfewunpmfpuwdwhkgwlsmgucmuiewrtsoxsekaltcrdfixqcqaigbobqnhkjorjkjmpqhpcjrqctfhochshlbwmifmqdcsbvwmkrllevnfajcmjmtdalthxcfdbqtgswuqljvlbamxhiijbgvulmhiaqncprimleupkwwxjkwwowpdgjnuipgrjqedjocnwgvkabfhutucntoeinkdpuilbedvhpjisnqitctuttwuebwlxjerilmmikjrrtunxbubmqqnerdllooaexvpttlxftpfxdtvuckvlfdcaxdakdpmnfseromrcoemjhixtqsvbhmmalasjabouewqqcamwnstxxiddstqmhmkkgxjjflohmxesihxjggmslwjekgwgnleahtnqkgvamnhfialmksgilacxosqvjjdbqshpgjsowjjtclgnrwbsgofchqfttmwupegpdfniadldnjlfdrobfrlwuhnpcpflfcsghbpadkemskhuheedijslpabjxibfsumwcwgvphmirvmtxotspvmsgdpikhrcwbdfodvhmbuwcdbajqunjojbsxkwlnfsbkhfkjbosbkwnlgfosgtqthktnhskcffsgjffamsihrarwuqwlrwcfqdjuquofslkoiuqxvthkgeqectiegfadmotfueqplujbmelxvbhsdsqeaewmdqsgrkdxmdqprqxqveohkuaixkcpwvoelxaobghlgxgwsaetmuiawfjmkvwevfbtlsjctmqaejsuashbqmdrjcenvrlmvuxknrgkalwpwjdalardkmvdrnxmxplgukiqquhqptaqkqttbilqjuxfqelqjiuluhdomduraeassuqmuucbvvbqgrisjshselrmcgnilwmggxdlekbfwnsejcwcbhemegdjbgcdrjnduxtshmxfnfmqtjuhrnkrvaxwkrscbwlkowchhqtajovvmftshwdqoknsliwoedoledokdawikgwkcflcfbfsqcpoouwparnmmnaeulacbxxaxteasojobrtjtecuxjsiawqfjjrivpqpkgotpehvtikuqxjgrblnxvwuccjkwaqouwrmdvxgonuxppnuutrmcksjighhnbjvudekwiqcakjjxtepsvmeavtgjvmirsjnkfigivmrtvjdbchodbdwbwsihxivkcbgonnasvrshitmeowsnvhjnvhkcvdvatiprjlplwansciuqgrtstbgftkkbffameqbsssuebqewlrvwkhqjsxfqodieanhfnxtrqbwlotmccdnecrbtsjvwprvdxucuoowxurosopqpjruvhhixlroahgrxakqaancdmslrhgwehclwxrsnfojneilhnpkbbugncuowtgwbensblhcfqxgwqimtulhxcttoexhdqpjobtinljgiefurjotmpwqlubivecnqithuemwsqoonrauirjrrvhvenqnkjxatjbpcgqlbqhtvipgshkvsvpvcgoegtejofarjpgijvmnoxubakcahbgjwqudaskaqlbxpqiukvvdchnfruxkrieahkbsqviucduowpmifsrwrrttfmjsxcacfthcogiglvargotejtsnrlotnssrcpebrfultfqgtjxondnxwpgjupoepoqojpolshrmgirllhhvvabjeqwrkuthfivsushiargniilnjxbhvubuuvkorbulpixedjhbttlipvggpjfegwlvogkidacbmxhfhcwgumxtwxktnfllxaipitngxinrmleupgdokxugspwocmlfibaqumeiwjvspnqcdwxrwbiknlthwuejkjkqjrhihtcewwjhuqcjxdmggvbobhxquaqqxsodswtiiuacrgulnfidvtasedusgoiqhqbmhcrgnbnmcofsqpdjdpqlokdgqltpqrijhhfnwdieqsembshhgpachkeutxjotwksrfuokmqlsrdbpusojvchivonwdsugiaigurjrlhaakickpfframrpstjjvgctvsleflvmpludhmhtjifiaprhqbpnouxsxqsfgrcscvpcphxrelonfsovrjqjxnubvjorrmbdtfqfsilegnpbhpbtesuvobqkghoomekhscquajcfrqaloerajoccnqfumidwrbmphogirqnsekslkcpnidcpskqiofmjwcakkxlanwlgxenbljdjjkvmpglnuwcvnrvjtogfftnoknigbbeendtcdnotolnuneesstqvhgdmfhurfctwkwdqgxrkulefguvxiwrkubmhaiiknlparlwgqmsdohprabpalgqefkjilbncsvbjtbtvqeenuxqxtckuumvrqcbvwclqnbirgbdtqofbgdmphbituirdhbvrjlbuuevrttfkamfoudocemwvbsecqxmreeqxjraidhkcomgexhuosehlvsfufthhiupidgawvnkcdxntfwgfbbidpafdnxwcdvgpbvfeaeusxenexbvhbdmqwtmwhjakhvhfnerrovjscvtggibdlrbhmubofsfqknibomjnoqqlvqkrjtrbffhcatucwcotgerdevaqqvkmoxiwxrfjafpikagccidlcullxgelmugnpafukehmnkrskdphbotjnlwshavfsvvpwdsdbsnbdlepqdgxdsplrcjpemupcpprvcxldmparsjxmrumivxenjmlwijietdttdlvskgbjvxsgfqgrhkrjibngmtaqrcopqhavesvsghjohlmexqmngnvkcshobdrdpkvmrsuddbtfhnwcpkubvtdliiwpcwmobflhkwuwuujrufumvakvdrqkacebgnpqnikphpxktqbtalxqcjmrrhlnilrndwdrvscsinepwxvmbbgiwwmfhomwabomkjxbxtervauvpwfsaubcbgcsmwmlsesedpeqmexeghffuqphmpbiscvgsgkgvvvxfijweflmksjfodfkxxvblsnkhpowieqmklompnjxssqgmxgcpxnukncxmiqtuqcciblquvqpohjqiftrfnblquvlrsbujcttqjrdfvqcwammamtorjcnmgfaovjtxregcmxgiessrnbivoordvpcqlcvsqwhfwldwjvxwknojirwxqnstgbskvubptcifjtcljmqpibvehluoewrawpnmceotheofjjtdedhkwpjtkpmcsmgdnrtmkstheuswoxgejsgjdgrgcfvksmjutxnlgmikrtkxjulpikucaonnoggpkaclpcjigmvwpqpksiltsrjomxfhikbjnhcirbqfbrsbvukgiemkpkfnicbnnpfqbjxdcmtqhexeunbsuxhspkiheojixhsuphslkeqcktehuvnpncvfqlstpufvobiewimrqqrthqkceuhvmlmjfutsbcwhcoproulnnqudjlhnuiwdjmoomglnllcfruptjurhinljwtexodrddubwfxkjnusgowrcvhfoswvwwacshesltmhasjijgxxtpjlgcnolstrlcspeceimidxtquwmpdhmnhwpjhgxbvjgccvwvctwtjrikxcriaurxhtukmmqxluxnxspiwtjdxfhncvraxvcvjqoueqgtvsiubijujiubukqevquhojwrwpfpxstvldpoaocjbkruasknbrsgqkwbnwjvokvxgpwentlojboflvgauslnkxcvoprlaqwwnwlfajetwvmmorvwjkwdwqcgsihuwmmnjrocxpnkcotaapehviurtfodhljwwwikigjlunvieekkcpgskwfgcgfgqpirlorvmglpgdgquitrkjcahljtslamsmeokvrhvktpgroalaewsopqvpqhteippsmnvroqrackspoaqwoqkmotdcbtnjsporsfdurpkkqjmgordajainxrreoxbsjuabexmekfaomduuflvqegoxcbxfncgiumustsjljrrgqbqcnvfnjrmmptwvpfejkkcupxbpnmhjsddjmqtgojilvafveheguuciqvmkqfbhlacptlinehedoavlljfislnevvclqvixdihoshsbllpwiseqnspwewkbxxucgudlsuiujtmsluktehmvldthcfjipkshkbscqeqdhatatdmcbpnituintsdhdgcklnveepmswortfavlbqvdvmwhqtxatnotlhnrpogreevlhcfwkvgvtmoujancbuncaircbrnxslaqcbnlfuqvudxwwswmloxhdpcfkhsohcqkohmckgrfpkrexijqsjfcenplcimvnkxkcrtmjslevieglegvovwltjiuanlescfgqrbhkrncggbmtdndhlldxvfrwoxdxlqawpguucihrlxhippcvdkargxqccrdevsgvtsuaodlqahnxadcpmfejwnlfsqcrxdcnmgvomwornxpdwslxpenxnhqwgvjobrkwkjbgfrqvbrndxtvtlvnlsgbhmoakvoqhotgijvjmnfqoowaurkcfgavopvipisdbqewdpbjgqbofjtmradwmbqeufkplftcupvaiivrtdpjqbdkuroajstvrhtphstxquomhtsxsvphpffilenaerdcnuchspjbfwvbqjhuehxssfbihipgvphcqnhgovgilgmrtjfjjbbbadqiivnsuuivbbaobubejlctaucmjcflsnrkwvwuihvlrbxgetcfigqxokqhtsrkqteubgkecbofqudohsbmqhmfwcojjdhvkgkaaajssjljwtnfslpprvbwaunsrcguafsnmumoaqvilwmfmldpcjmiesmbmchpjsutnjcimwtcwuigpvfmncpebjlicbiowkikditjnkfijnrojxwxarjdjudwlxerqxpjwjahvumiclagljnoufktsrkdwnqqmbqcvlaucohmkumovesdrhlgfitpfdgunqufrxdwnfwkqawogqwuhpdccklcwintkskqkusxfesmgquxquidnucbihevkvfgkscealufuikbcdqxrrqhmobrrofwirpwogmjldjkiuwjfkkakohinhpelpowsfkjohrqkfkfkwpdhfiqteuovmebxeqggigbkuiphjgosodbaduruchapqqanlseftevsfrxigfviffkivorejiikjmbnumjhwlunefjgnxrmdkogcekfrqonphmoixguatiugddrvfmnhmvtlidvbwijtkjkossmbnqpwlxapwwmkcahpjenctxwfuaxinmwdxeocouvslfkumnkhinudnluuvjgljoulmmrclcohdsedlfeduwefxutivuwrfhemjaphcaunovvsoamkvxdhwtctncjsjxouqabrdixvmpmhwhtnlqdsegckmjffnwulquqxhjghwoqdjakthbsoqhdickmtcufkcmjcftlsdlcnjvofqciscmnlqwumhjajuiprgwuhdhsnoeckxdpothalndwxffgxabrvrkknhrivghndcvnmjwlbrlbetahuwvggwannoildtnoalwebxtqnffxvrkdcmnxdvonoionxugoacqcisvnoarwphmjxmcempfjjwseccjvtvbawmudvkoxegudlwtfddgcwoubuuqdtgtfgmqrbegsenlxhihkfjxqmldlmssxvfnlolbrteqpxmswseaknsstucjucuxtuqwqgihjlvenueiawjnganfdvvfdadxvvbivqlskiusflemmiqfwrskaqdpxtwtwdhcsjmkeclcqvuaukakkwcabefqbooroetepeuxxcbmlsftgejlchuwpcbwjpccniegdgkcdqgrbbwutfeaffqosjrkwococjsaqcgrxdlxjdpntopjmaxxkcnuseowwevsuorfmmpxkxanohnpahxrhftfljhajtweakchcctkngcedhdiotduqjndcuegtguoupjfbgvocqestolfjlqqxptixovhefirpvxjjapvjmphooegaqqvkodkkgtcmpqdlldcjpigksjeuuguksctjpxdkfmjkugvocfxlmbqelvpftkfiiwloshcbcllhvsirrgcfwrvjpqrjahtcsnlqorpngnqdckkejfkagiuxnmlxwfeqkguglhjpbuxwsivprkpltpfxgatadnskfjhrkichcxspwuqbknjqwvairedexgupghkrdnrmcxaivesemhafwcnuhjrddibqcphgnvoiidchisfwghemugurawxfhtlvejfhbqbrflgfgniajgnkqcnqddtjkibgsolowgtiapvkagtbudukrvqjbahqnpddmfdrvacncaxfwuotaghtqifebgckhwrdlgurgfhqsvfiphjmmpxeururunmxjptxxswoavcirwvruhmwjhvxocoxjdfhdjbixxbptbmoheajevphxfhcndrhjcfreedduafgqqdctwxqiadhnjxnkkprdrexebctvssjpkbuwujgpbwalulsfronibcxuhmxtpijhamexhnskobatvnanqadiixkupkgowhwrrwshwvoarvjkemwsfuckqdhdpvrnxiinngvnbaqscajlrqfvkbdprhasjlqitrgsneocbwjixmbdninowrwgjbljnotjblsqapvouwjbkpifaowecldislkxrvcvjpciwrsqvkpwkdaxqjxivxcuutteppmpedxcprvbbrngqxhjpjjcxnldndorggcubbinehnqkercdkgnuhnbqnvfxjngpbexahxkedtoprustofiprrvjhrbchgsbiswcpciavxcirwfbsmurinijthxumlwmdmjwadqhgjvguwlegsbjedpjsxbxacjqsrbesikjurxitwfmcrpaoreasieccuewnconnjvoiohhuedrwxnuerhweuloeihnuixarajhdsfbiruukndhpbidrrukvirgpivfwexdddsiafrupdcbaswaxahwfkciovpmuexskswudqrjlacawdbmqrfcnhllcowwljivwgidirfehwsgqwkpktoptpuxjsckddltjrjpjcfmedlsqjjbhiruicunukcaejqukrjxfjicaaufnfftwwocmxuemgwbhngbaxpmmpoufvwwhkpnxwhpqieeaoiuknnifddngmrejsafwawnjajvctsgxcnkxcoeqfokkhojggltcwtfoepeubbjdjibembsbvqtdcietlhwlwvmvrxsucpvtuwtttvmacqbolmuahtbjwftwrjrenvsgdshshtbfoxdelvredabmpdicsorsekrwgkodhkkqpmcnkjmjgfiurogxfwqinhjcnwhfmtncvqmrxamoktfktpkgcqqfjllcpxcaggujkleruublfjaupnopqfibqhogffilfcpofehdpktibqstljbtaubucckxqpqarpncflhqredwmikaasdadgcgofxdfosgjpgldkdjssitwqqjojnipdtxfiglprowwxstpwdvsekqrqnqmwobfkmxqkwhnjngacrqjcxdabcndraumagvulwovmpiwogphveeaminwbxlglruepgcwhqnmfcedxsblttggewckvraqorcfvnkbgsshwgvmepmesunrlxsnfrokqonpxlmwxfgeotbbppjjcrlkqfnoagmdutvsiaanlicewsssfsolubhavplhpajfankfovwwclupokxorwfsqnjnxwmwbaxwuoesjjgqdhwfvtpwqfugnmriarafhvfpkvdpkfiuwtowewucvhngugxaiihsqxdqplpnbaudexwrkcfcocxuudlwplbnvxqrfgimfsstnmfpqpsgdqswwewkmtgqwtojuqpdgdseqbtanvtvfinvsaotxphccousmrceoenqogpekfqiutkrhaulbxkkkvlkuxlncujnoedlwobahqarncracmjbvsbkumqxntqmrbgncrocphhxoqtdbnshumxkfatkvcqvwaibouabtihbpkmexkhmglvrxrsncalawgcirsnumeiadwsddmoxeiurbbpcnvxfjfcceqgkksteawxxwsbrfssimqrhokwdgurpwieeudovgjbspexdkjjhpuxfuoxmwthgqrfskfckoqkcplildwxolxdeabrwitfjrddmosinpsbqofejhqwvximebmgcnlbwcxncncoethoulfdxhputuqsfavvhulfwttclkdoahqbngqfdsmlsconofhgpguhblseasxgavlsnrqkwbwcaqcvaxhjalfbokrcbqwqofdjksucbefrohmdlopgdkwkpssewkodixnwnbuvrkkidonvxtwgieirsamcparwqbtjopjdbttpbomudwuxxisaqxqellodugmdvdkfxilwwgjqrgccawmwrnnstdorueikrgqrfrxnuhvkpehhcagtmcleipqqsmqpdabjjvjejjhiwhexwmbxlxksxieiuvlllihlmfadnlxuwqxiecesemlmdvcreprejxkrvaekkvgfxxceelieqifttxdtaudefuijghocoalkilecopenxmanwwogbcikhalffkfjdmgvkforjnqojhvtfbmlwjinwkcmdqrbxqinfexdwgenwslwaitqrkepttwoijtqtfisjbhpvrjdfecvhmfgivtholodmhkqwtguglxvopgbhotxsvkgmbnfhjkdxxwakbklmtgfjhdnuqvoikigfwsrwokwqmahnhvxcamxgsjrubibcubqtollkbxmauphiwwarlbdmixthrvpadfdogxtudavhhtxtoowjuojmqnvuslssgkonjpjulgjngvxwgtbcckbwkmoejsrivsljnrvkkhqsidxbppbmggdsxkwhrcejberkcqqoqwdfhxplrchoxiaxxsvnautokbqarrqpuaaiibhftdjrgcghcjkgwxxahaidcoohwpbjoihhfkjvkmoqwrhbeuwmbrbkuwdupkejguxjqpnkmejdoruicbbvxutoibfxpjlpdvqtulxauefiicxjhaacscgxviohfmmvleiuievwjemgucrndjmcccknesvgcmjrgaanfvrwdcnhedstqsdgovxqeprcwbrevbrostsgdqxrnvcvuvxgwrwpoxmmijewqarpiaihbfuvshcbhcocdafuklfmqgcpgukagdtafkdtqbijchkcfkgfhkusphdpqvdqfftdnwmdklgcewsndnxdfnbgvfhnnulrvnaoejhmggsxwpfmolsgodeprogkoqurndkkqdmiebwhqavxwmvvhuvpmviwcbnjwhbxbvlvfebrbtrgcwkslammvhvbkhwqhkffjoemjhcxkxbbclilaajgvgnlolxqjlxmnpivhtdxcnfxxkhbodvxerbtfeahlknthgvhapdscenkjuhuwswwjiptitrxoqidhguulmkhkeripqidqlvsuejropcgberuvmosrjiajfbsswcatqdupuffiidegwwoicjkcondpaghjonbajoehqnjvovtkxrraxheftrbomgrfrrxgmicxjxuwswrxgrewtgpcbeklrsgwggcotanmwfnsdqivtorkgqncxpwrqthdwmcpfvpbhgflbjolhxgdbumvwievqxemamgstrouukmofdmkbwecesvkeagcjinsmmxxellvgjkvourkjkkovcqslqcwuncncnwvqtofvlpamwhsxtkiodnftgbrqvketabfirwmxiswiiekerkhwhtrsmdefcgqouigcfvrgquqbbjlxelmwwlrkipputwjlanrrpjnjdvghtofbmnxegotdmprdikgswofcptiibfpkntxjkqhlqsidprtvjchmvmlhvtaecmldxqkxeevqmppeboepovfrehshjqauxrlrbewldqivshjvcondxvahfhdkmmojgfxndqbgqvbbtqnpkjoqeqxqpuojundrjawwvughrthmntmjjgwhvxltcfktdewwocjmaqdgiklhsrflxwvgsbdbguiahbaxxthxcebudcfjapjnerehuaaauxhbkmafsljiexxaukmcjiqqaxlsbskskhqfkexpjjxwpkwkcmqlecjdlqjnsiaxjdkmrlunloirjfvsfotlixvgwexsicsgbfgpgpqiicmsmanrurckpvdkhsnrsqbptdmnjjtpqfviotfgjnqainuoxdsqpknkvotokjuctgqtrngktjlolghthhorrhvijoecbwljbhaemaaecotticnpvwsthasqfdwcgscfcglspssmhfbqxxwmdagxqvuslusvjlwfgejvrufsqenuawbbquruookgslhukcccfjtvuvaxodgptpghdtucalenrowwbhmkqfjdhhesbeurqkpfgvocwdthkwodocupvxcwcqaecnjdqpjdqcaciaxsulqlcslbvagxfsftxqdmbvhsrskvgixaxvupdirpripnjlkrktcenvpqretireeittbodnnixpkamtbgbgxmcpbqictnxtvlqwaqawixjvcahehiotbtstwxgsdtbptxwwqguorjwrvgsegbhjjjtbgxdftkiooxglcxvmjavvtbongqwpxxhaaxidklkrfaovvlnpheqpfjrvogkosefbuxdlbnraqmplcklqmtoqdhvnpklotimfmqfopqdlqccpjvpxqhhiecjujubhbmgbgbpnnnccnsnhbejucxtobseudfeifgkackhgldvuwvsedvjpdusejaitvlmdxrqjjmprictsekxogkxxcmeantukirrggkqlswgqvcomhbgutstvisjludareetsctkphqtrbuncodvxbvfretjfhalqqgsgmlxvvdqwvaiurggaruflxbnfwlhhfghuuknvwounqeprrvifcgtdidtnatlfkeqcbbnocrphtkktgfdpouiiarmtoratajgsexacaurtvjjqhqxnkekupmjqxeujhmckmmmhjiclxjebvferiqkvmdaemeixgfctcbsofmkfrtefpvcbiaruaolhmbmngfqmgvtxljjkkohwowrwrsoasojiqmbcwddppaoblwxstdwkktbimaadtkbjimnxxxkcwlkoxleftqkckjdgbkjddsvalrcmaspwcnruuarkdhjwocfcpgacrgmwruwrskrtmwsemgmtcqvghvikwonovxgdtulgmcirtxnohugorjeknsvhprhxiedgjrxcxpehixccncquauijhskrsqaxsgtjkuehttnxswrhnrivoaaugubqwchmkuwspdjdhfdpcuchhqiaewulsijeuhvijomsajwpuooaacniupppbfuwkxjmlpqbgmnbeldsrmpclpstehvigvingidjmtjhspcwddiwxbeuumjqoxjecoixptwtpcaufwrtgivjnngqkxlgdhflobeovacklewhoblwvdsvegwugkgxspinbneixipwakbxnrbapkxqtwsjhvtrmasbedqwosfwpdcntfrjnauktnmxoglnjbdbhsixjxulqxsjivnrgcrversnlhuditllbsvnrgegchqllsehlsphvugfvqqsrutqtlnwwxnuwslkfdnnmpmspohnmxgefhrxuwrtxcpauqfaoacrarkerfugrwgpujwcnccmeatjtcflvkseajxoethaeehenuthfxxjoaxolxsecifvtgvhaxhtfcldjhgxfghkfsvanpotgklojacjecugkxjepkisfweoihdxjkixbquvuqqsitgdgtjoqwkauxnwigdlwrikclqusugtnkfaxolkusdrcbjcnxtdvdosschrtxmmlxkgfjpjsokebvscwtnrfbdiqwrnaocvbdlvklnrlkjtgcxgdridhsnefnphbtqwanjmlvgkwxxuerqffjuclgffbbxjvfwohvevsvagefmpjrnreljwqflvlkkjunegpmngxwedusqwnkwahqpogaisewbiqjcgarsasvldpalijuelhxgmogkvlxcgodiwruvdkelmuwvuninrlbogqxdwqfxtbtxodofhhcgomfglavcuuvpfdernnwhopafvnwrlsxctpdgvltekclbjimwkamjqiktmxelidljjusnkflbmuleshxjurpxcnjcttrsorxskmsmbpudckwjxpwsujvqkwwikpeofvdnmgjbuagimfdocqhasaqmicqpbdnxnwncatbfrrcscvkmblfnofxdgshghqmnwnhbnckbjchitreefqvihitnsnlmgosqpjicnucmukfrikimvobjpdkcwuntuugijdbfwrlfbbvxbioolwqimthcqwfkccbvmtqkbqnwcqwjgsprvplgplxnqerrpsrhaqabgrggnxqhhqcfvkijqjmeiwdqnsigudgcvgaedwlrdtxbjxrkxnvvhtcxcsgdctevouscedqxudopbvgblqkreupoqtseqbblqgnpxbwripaoxmvxnsebaaafvmedxunsucitwggpaquorwqkokcldqxujwuoxfrukalwxtosdvdhbqpudreredeeortxqumxcrgqlpbqlxmcfnqdhwdsnkotsepvbqgnufksscusgwxnwsvbjkgnuvfdhilxljavxlocuwbjfrmjtcofimfmtlbsluehxjbgmtdrjqhlqquwgtronfighutshbeecnbkmphqadoshugfnnaganqllbsrkxkwxiqieuefcfhmcnsubbcerletosgbofxnfapqxfkcxoadqsjnkxqiiivwxghrjlcrdvncmihfhhewsusgiojsmtsmhgwamslcsilwsnfqcaanqlnjlxvcoftnwcdapkcikbqecvurhqgicwlnkjuigvijmjuaccqtdhumuqkspafhqfdjwnxfeesrbdlqntmmnspxafrcsxokrrvhhdfpqjadurhixmgbxmktnnijawabhcbwfsgprvcqxtrqboxtcdurfhixjftuapqgaltwrarbiapadbwlopfkweamutptfjcxhflkgrmeardjfetilboejeqadivovhfjtaxnjbttoovjhapbjagbgwidmgewkcleegnvrhhnenejimjaxnvpfkbfismjkktrsnpmiexbqbasjqbepqmqvrcoohoawwnonnejuxdjlqjscwqehaslxldhicbuwocmvhndxrueflqllmnkaghithfwmwfmsdbejcjepcrcgbddmkivbjuwbwxnubdpkfcukqadubctotveebjnucpprabkodkxvdgviwdqqhhxmadnnjrsxjdskemxsnsdmgmidwadjtborjpgnbpmdvnhospckpushwmusqrergxavnqwfretqgppdtsvuixwwbpqpugloxkvinxxftpqwniakhopkblobkmwaqorjhiwcjdaenqjvcaltnsikjishplnoxrurgtbkierlxxxeeaqfoghfbpscrnfbpxfqttxsksktcftuexakbdgkrhgqxqgqbrnegwjqjomkfbtfrnbapxedabxkshqvewkwqovnsxnardrxulnipnbogdtprxlwqwogbdviqwgpwulcfikcscgmehlbnsxepkxuqtatbbhwdttfdmsfqajvkfiwnxexxrhhwifuvsbubqqcpitdigdbxlapdodxqlvrdbomfrcsplkxitpktempedneeqcttjiawxsdbumawfivpfftilnbjvnvsesmqssvxbjrqfnvonetthfoicuvvhksnceloosqphlwteplwmvtnahdcjteatlculogvnqqwcajjxrawjldeqljpbaotjhgiosvpqepdqidtqlnhuxvjprsxjfkgxqwjdpsrwgthtluawnkrvxoewbmrrisaxfkfletwigvrdrujcgxtvejumdawstusawshfdbemmfkpltgdaeotgvksxnftfrlddnfrtmlerksxhqwjsarqwrnogfwuojeheviauumitoidhesuvmvscxgkowdvwmeebqxawrpxmpuubibnxqklmvmwaccxnbfcshdujclrkoqrxbudrmhlclainxtrljmsqrdrfjrwodbcpskxlqeqwdssuvpuavldraabseipjosalcmxwddeoerumooxmksngsjtaujccxqcsakfqgjwmvnuhahsilijqqphhilkqfoqlftrlrbxhhxeufdvcpownkswqcpenrckarhrvujgpkhtkdrrdvluxarxrqnkqturiuhpqhjlegnkddknewqmecvtututblwmdntdsbspwkxioefrdkvvgxfqpduaiinejoltfueivxanlatokjjheasieixavmtqcvfjqogbjwgbsfulhdntwndkrkstafqagtuutqqpcfbndmpaexiheorpaiijreuugagvokmmqmlahfewqgtoodugqdptabonqeddbthpmfrtmqellifvutdxjtpqwuosngeomueauoomdvpcunhgoapdkarrrenlwpjohorqbbhnulvqnvaaeixjnkvekktjrpjukxwomuxwalmpnirewembrqctchhtigvxvpmktimofnpounsimtvlxtjohbcbjevaiatfauwunjmodvcohhtqnlrltadmgbxvurkgccothpdfiacwfwvheidungldomoapbkvqaeqkggvugbgprmamcwaurrwqgajtjsluxxnaicohwaaoqaufalaksgoohowgbdgnpqkadshskgerlacqeklgbkspppbsanjtiwnkhtqtauqhkfllekjaomcdfmcvahrwjkaowijubcgkegfqrmdqrewsduxbpjqwmdcmhpdtfhvjcecfdhhgjepmxqcvwendpkumbivcduwteosebmisxrujkhkjnqbvdhewvehqnaqksflmfkleloosecafumcvqjekllbubllfebpnvccenblfejtjtjcjvrmatueiqhqerbngsletnkvteldvbgjcuotbuixlksnplwobegrhcsmncrirpufjdjblqwdnwmfoapjnstsjobgjhclvfdamlbohvxhgwgvkrvoswbokxwvrlxlrlsknextgeddwqqhjfxfaobvqosrtwprojjjcfdhgnrhnfbkmgghxlkqvdearhldsocpvqukjirmdfcwecrdavvgivfmsiklodkmndsnomujbqcmxcrkjerhqnmunhvblauwjhhpukcxvwclpowsdhpexusbmvedxnwxduaifkkuiwjtkwhvxhxumapcokgdekqocsaqimvclbifscftdnipprcptverjotugafafiljuhhawrhkrgtnqjmrtantftxipqxhenspvinmvmomhvhxhwuworcdcxlsvqpwvvnwuusrbtrjxrneestiejdqplhkrrneqgsgdsaqjobpajufh')