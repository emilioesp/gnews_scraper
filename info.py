'''
countries codes source: http://www.genealogyintime.com/articles/country-guide-to-google-search-engines-page3.html
languages codes source: https://docs.appmanager.io/docs/list-of-supported-languages-and-locale-codes
'''

#Periodicos
argentina_periodicos = ['www.clarin.com', 'www.lanacion.com.ar', 'www.pagina12.com.ar',
             'www.tiempoar.com.ar', 'www.diariopopular.com.ar',
             'www.cronica.com.ar', 'www.laprensa.com.ar', #'www.ole.com.ar',
             'www.ambito.com', 'www.cronista.com', 'www.baenegocios.com',
             'www.eleconomista.com.ar']
argentina_periodicos += [x.replace('www.', '') for x in argentina_periodicos]

brasil_periodicos = ['oglobo.globo.com', 'extra.globo.com', 'www.meiahora.com',
          'www.odia.com.br', 'www.lancenet.com.br',
          'www.correiodobrasil.com.br', 'www.jornalpovo.com.br',
          'www.jb.com.br', 'www.folha.uol.com.br', 'www.estadao.com.br',
          'www.agora.com.br', 'www.gazetasp.com.br', 'www.metrojornal.com.br',
          'www.valor.com.br', 'www.r7.com', 'www.supernoticia.com.br',
          'www.em.com.br', 'www.otempo.com.br', 'www.zerohora.com.br',
          'www.correiodopovo.com.br', 'www.diariogaucho.com.br',
          'www.alo.com.br', 'www.atarde.com.br', 'www.gazetadopovo.com.br',
          'www.dezminutos.online', 'www.tribunaonline.com.br']
brasil_periodicos += [x.replace('www.', '') for x in brasil_periodicos]

chile_periodicos = ['www.latercera.com', 'www.emol.com', 'www.lun.com', 'www.lacuarta.com',
         'www.lasegunda.com', 'www.publimetro.cl', 'www.lahora.cl',
         'www.hoyxhoy.cl', 'www.elgraficochile.cl', 'www.df.cl', 'www.pulso.cl',
         'www.elmostrador.cl', 'www.adnradio.cl', 'www.t13.cl', 'www.biobiochile.cl',
         'www.24horas.cl', 'www.cooperativa.cl', 'www.eldinamo.cl',
         'www.duplos.cl', 'www.radiosago.cl']
chile_periodicos += [x.replace('www.', '') for x in chile_periodicos]

ecuador_periodicos = ['www.lahora.com.ec', 'www.elcomercio.com', 'www.ultimasnoticias.ec',
           'www.metroecuador.com.ec', 'www.primicias.ec', 'www.cerolatitud.ec',
           'www.ecuavisa.com', 'www.expreso.ec', 'www.vistazo.com', 'www.eltelegrafo.com.ec',
           'www.eluniverso.com', 'www.primicias.ec']
ecuador_periodicos += [x.replace('www.', '') for x in ecuador_periodicos]

peru_periodicos = ['www.larepublica.pe', 'www.elcomercio.pe', 'www.diariocorreo.pe',
        'www.peru21.pe', 'www.larazon.pe', 'www.laprimera.pe',
        'www.expreso.com.pe', 'www.elperuano.pe', 'www.delpais.com.pe',
        'www.elperfil.pe', 'www.exitosanoticias.pe', 'www.trome.pe',
        'www.ojo.pe', 'www.elpopular.pe', 'www.extra.com.pe',
        'www.elchino.pe', 'www.elmen.pe', 'www.diarionuevosol.com',
        'www.diariouno.pe', 'www.lanacionperu.com', 'www.publimetro.pe',
        'www.gestion.pe', 'www.perushimpo.com', 'www.lapatria.pe',
        'www.cronicaviva.com.pe', 'www.peruinforma.com', 'www.dsn.pe',
        'www.andina.pe', 'www.laprensa.pe']
peru_periodicos += [x.replace('www.', '') for x in peru_periodicos]

guatemala_periodicos = ['www.prensalibre.com', 'www.lahora.gt', 'www.elperiodico.com.gt',
             'www.dca.gob.gt', 'www.nuestrodiario.com', 'www.aldia.com.gt',
             'www.publinews.gt', 'www.soy502.com', 'www.nomada.gt',
             'www.republica.gt', 'www.guatemala.com', 'www.newsinamerica.com',
             'www.ojoconmipisto.com', 'www.perspectiva.gt',
             'www.elmetropolitano.com.gt']
guatemala_periodicos += [x.replace('www.', '') for x in guatemala_periodicos]

el_salvador_periodicos = ['www.elsalvador.com', 'www.laprensagrafica.com', 'www.elmundo.sv',
               'www.diariocolatino.com', 'www.elgrafico.com', 'www.lapagina.com.sv',
               'www.elsalvadortimes.com', 'www.elfaro.net', 'www.contrapunto.com.sv',
               'www.solonoticias.com', 'www.ultimahora.sv', 'www.verdaddigital.com',
               'www.diariolahuella.com', 'www.elindependiente.sv', 'www.elurbano.news']
el_salvador_periodicos += [x.replace('www.', '') for x in el_salvador_periodicos]

honduras_periodicos = ['www.latribuna.hn', 'www.elheraldo.hn', 'www.diez.hn',
            'www.diariomas.hn', 'www.proceso.hn', 'www.hondudiario.com',
            'www.tiempo.hn', 'www.ellibertador.hn', 'www.confidencialhn.com',
            'www.enaltavoz.com', 'www.elsoldehonduras.com',
            'www.libertaddigital.news', 'www.criterio.hn', 'www.elmundo.hn',
            'www.paradigma.hn', 'www.quienopina.com', 'www.dinero.hn']
honduras_periodicos += [x.replace('www.', '') for x in honduras_periodicos]

colombia_periodicos = ['www.eltiempo.com', 'www.publimetro.co', 'www.elespectador.com',
            'www.elnuevosiglo.com.co', 'www.qhubo.com', 'www.diarioadn.co',
            'www.larepublica.co', 'www.portafolio.co', 'www.lafm.com.co',
            'www.elcolombiano.com', 'www.semana.com', 'www.pulzo.com']
colombia_periodicos += [x.replace('www.', '') for x in colombia_periodicos]

dominicana_periodicos = ["www.listin.com.do","www.elnacional.com.do","www.hoy.com.do",
              "www.elcaribe.com.do","www.diariolibre.com","www.eldia.com.do",
              "www.elnuevodiario.com.do","www.metrord.do","www.ciudadoriental.com",
              "www.ultimasnoticias.com.do","www.acento.com.do","www.primicias.com.do",
              "www.almomento.net","www.santodomingoadiario.com","www.diariodigital.com.do",
              "www.diariodom.com","www.eldinero.com.do","www.diariohispaniola.com",
              "www.diariodominicano.com","www.noticiasdominicanas.com",
              "www.lasultimasnoticias.net","www.remolacha.net","www.elperiodico.com.do"]
dominicana_periodicos += [x.replace('www.', '') for x in dominicana_periodicos] # inglés
dominicana_news = ['listindiario.com', 'elnacional.com.do', 'hoy.com.do', 'www.diariolibre.com',
              'www.elcaribe.com.do', 'eldia.com.do', 'elnuevodiario.com.do', 'www.metrord.do',
              'www.ultimasnoticias.com.do', 'www.acento.com.do', 'almomento.net', 'diariodominicano.com']
do_news =  set(dominicana_news) - set(dominicana_periodicos)
dominicana_periodicos = dominicana_periodicos + list(do_news)

mexico_periodicos = ['www.milenio.com', 'www.excelsior.com.mx', 'www.eluniversal.com.mx',
          'www.heraldodemexico.com.mx', 'www.reforma.com',
          'www.publimetro.com.mx', 'www.la-prensa.com.mx', 'www.elgrafico.mx',
          'www.capitalmexico.com.mx', 'www.jornada.unam.mx',
          'www.unomasuno.com.mx', 'www.cronica.com.mx', 'www.razon.com.mx',
          'www.impacto.mx', 'www.elsoldemexico.com.mx', 'www.diariodemexico.com',
          'www.contrareplica.mx', 'www.diariobasta.com', 'www.periodicoeldia.mx',
          'www.reporteindigo.com', 'www.elnovedades.com',
          'www.miled.com', 'www.pasala.com.mx', 'www.thenews.mx',
          'www.maspormas.com.mx', 'www.24-horas.mx', 'www.record.com.mx',
          'www.esto.com.mx', 'www.elfinanciero.com.mx', 'www.eleconomista.com.mx']
mexico_periodicos += [x.replace('www.', '') for x in mexico_periodicos]

nicaragua_periodicos = ['www.laprensa.com.ni', 'www.elnuevodiario.com.ni',
          'www.trincheraonline.com', 'www.bolsadenoticias.com.ni',
          'www.100noticias.com.ni', 'www.confidencial.com.ni',
          'www.el19digital.com', 'www.articulo66.com',
          'www.nicaraguainvestiga.com', 'www.ipnicaragua.com',
          'www.nicaraguaactual.tv']
nicaragua_periodicos += [x.replace('www.', '') for x in nicaragua_periodicos]
nicaragua_news = ['www.laprensa.com.ni', 'www.elnuevodiario.com.ni', '100noticias.com.ni',
             'www.vostv.com.ni', 'www.confidencial.com.ni', 'www.articulo66.com', 'nicaraguainvestiga.com',
             'nicaraguaactual.tv', 'ipnicaragua.com']
ni_news =  set(nicaragua_news) - set(nicaragua_periodicos)
nicaragua_periodicos = nicaragua_periodicos + list(ni_news)

uruguay_periodicos = ['www.elpais.com.uy','www.elobservador.com.uy', 'www.republica.com.uy',
           'ladiaria.com.uy', 'www.montevideo.com.uy','www.lr21.com.uy',
           'www.eldiario.com.uy', 'www.subrayado.com.uy', 'www.180.com.uy',
           'www.ovaciondigital.com.uy']
uruguay_periodicos += [x.replace('www.', '') for x in uruguay_periodicos]

paraguay_periodicos = ['www.ultimahora.com','www.abc.com.py','www.cronica.com.py',
            'www.hoy.com.py','www.hoy.com.py','www.paraguay.com',
            'www.lanacion.com.py', 'www.npy.com.py', 'www.5dias.com.py']
paraguay_periodicos += [x.replace('www.', '') for x in paraguay_periodicos]
paraguay_news = ['www.ultimahora.com', 'www.abc.com.py', 'www.cronica.com.py', 'independiente.com.py',
            'www.hoy.com.py', 'www.5dias.com.py', 'www.paraguay.com', 'www.elpoder.com.py', 'www.elredactor.com.py',
            'www.lanacion.com.py', 'diariolajornada.com.py']
py_news =  set(paraguay_news) - set(paraguay_periodicos)
paraguay_periodicos = paraguay_periodicos + list(py_news)

puerto_rico_periodicos = ['www.elnuevodia.com', 'www.primerahora.com', 'www.elvocero.com',
                'www.metro.pr','www.noticel.com', 'www.periodicolaperla.com', 'www.elexpresso.com',
                'www.telemundopr.com', 'www.primerahora.com']
puerto_rico_periodicos += [x.replace('www.', '') for x in puerto_rico_periodicos]

belice_periodicos = ['www.sanpedrosun.com', 'www.breakingbelizenews.com', 'belizean.com',
            'wicnews.com', 'edition.channel5belize.com', 'amandala.com.bz', 'lovefm.com',
            ]
belice_periodicos += [x.replace('www.', '') for x in belice_periodicos] # inglés

bolivia_periodicos = ['www.la-razon.com','jornada.com.bo','www.paginasiete.bo',
           'www.erbol.com.bo','www.laprensa.com.bo', 'www.lostiempos.com',
           'eldeber.com.bo', 'www.paginasiete.bo', 'www.eldiario.net',
           'www.noticiasfides.com', 'correodelsur.com']
bolivia_periodicos += [x.replace('www.', '') for x in bolivia_periodicos]
bolivia_news = ['www.eldiario.net', 'www.la-razon.com', 'jornada.com.bo', 'www.paginasiete.bo',
           'www.erbol.com.bo', 'www.noticiasfides.com', 'www.boliviaentusmanos.com', 'www.laprensa.com.bo',
           'www.oxigeno.bo', 'www.brujuladigital.net', 'eldeber.com.bo', 'www.lostiempos.com']
bo_news =  set(bolivia_news) - set(bolivia_periodicos)
bolivia_periodicos = bolivia_news + list(bo_news)

costa_rica_periodicos = ['www.nacion.com','www.diarioextra.com','www.larepublica.net',
              'www.lateja.cr','www.elmundo.cr','www.elpais.cr','www.crhoy.com',
              'www.teletica.com', 'www.elfinancierocr.com' ]
costa_rica_periodicos += [x.replace('www.', '') for x in costa_rica_periodicos]
costarica_periodicos = ['www.nacion.com', 'www.diarioextra.com', 'www.larepublica.net', 'www.lateja.cr',
             'www.elmundo.cr', 'www.elpais.cr', 'www.crhoy.com', 'elguardian.cr', 'amprensa.com',
             'ncrnoticias.com', 'elperiodicocr.com', 'delfino.cr']
cr_news =  set(costarica_periodicos) - set(costa_rica_periodicos)
costa_rica_periodicos = costa_rica_periodicos + list(cr_news)

barbados_periodicos = ['www.barbadosadvocate.com', 'barbadosadvocate.com', 'barbadostoday.bb',
                'www.nationnews.com'] # inglés

trinidad_y_tobago_periodicos = ['www.trinidadexpress.com', 'www.newsday.co.tt',
                'www.guardian.co.tt', 'www.trinidadandtobagonews.com']
trinidad_y_tobago_periodicos += [x.replace('www.', '') for x in trinidad_y_tobago_periodicos]

jamaica_periodicos = ['www.jamaica-gleaner.com', 'www.jamaica-star.com',
            'www.jamaicaobserver.com', 'www.jis.gov.jm', 'www.go-jamaica.com'] # inglés
jamaica_periodicos += [x.replace('www.', '') for x in jamaica_periodicos]

suriname_periodicos = ['www.dwtonline.com', 'www.dagbladdewest.com'] # Holandes
suriname_periodicos += [x.replace('www.', '') for x in suriname_periodicos]

guayana_francesa_periodicos = ['www.franceguyane.fr', 'franceguyane.fr'] # frances

venezuela_periodicos = ['www.ultimasnoticias.com.ve', 'www.eluniversal.com', 'www.2001.com.ve',
             'www.correodelorinoco.gob.ve', 'www.telesurtv.net', 'ultimasnoticias.com.ve',
             'www.elimpulso.com', 'www.elnacional.com', 'www.el-carabobeno.com', 'www.lapatilla.com',
             'www.elpitazo.net', 'www.noticierodigital.com', 'elestimulo.com']

panama_periodicos = ['www.panamaamerica.com.pa', 'www.critica.com.pa', 'www.prensa.com', 'elsiglo.com.pa',
          'www.laestrella.com.pa', 'www.midiario.com', 'www.diaadia.com.pa', 'www.metrolibre.com',
          'www.panama24horas.com.pa', 'anpanama.com', 'ensegundos.com.pa', 'eldigitalpanama.com',
          'lagacetadepanama.com']

countries_info = {
                  'AR': {'name':'argentina', 'gl_language_id': 'es-419', 'newspapers': argentina_periodicos,
                        'topic_id':'CAAqJQgKIh9DQkFTRVFvSEwyMHZNR3BuWkJJR1pYTXROREU1S0FBUAE'},
                  'BR': {'name':'brasil', 'gl_language_id': 'pt-BR', 'newspapers': brasil_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREUxWm5JU0JtVnpMVFF4T1NnQVAB'},
                  'BO': {'name':'bolivia', 'gl_language_id': 'es-419', 'newspapers': bolivia_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREUyTlhZU0JtVnpMVFF4T1NnQVAB'},
                  'CL': {'name':'chile', 'gl_language_id': 'es-419', 'newspapers': chile_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREZ3TVhZU0JtVnpMVFF4T1NnQVAB'},
                  'CO': {'name':'colombia', 'gl_language_id': 'es-419', 'newspapers': colombia_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREZzY3pJU0JtVnpMVFF4T1NnQVAB'},
                  'CR': {'name':'costarica', 'gl_language_id': 'es-419', 'newspapers': costa_rica_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREZ3T0hNU0JtVnpMVFF4T1NnQVAB'},
                  'DO': {'name':'dominicana', 'gl_language_id': 'es-419', 'newspapers': dominicana_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREkzY200U0JtVnpMVFF4T1NnQVAB'},
                  'HN': {'name':'honduras', 'gl_language_id': 'es-419', 'newspapers': honduras_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRE5vTW1NU0JtVnpMVFF4T1NnQVAB'},
                  'EC': {'name':'ecuador', 'gl_language_id': 'es-419', 'newspapers': ecuador_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREpyTVdJU0JtVnpMVFF4T1NnQVAB'},
                  'SV': {'name':'elsalvador', 'gl_language_id': 'es-419', 'newspapers': el_salvador_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREpyT0dzU0JtVnpMVFF4T1NnQVAB'}, #no arrojo resultados
                  'GT': {'name':'guatemala', 'gl_language_id': 'es-419', 'newspapers': guatemala_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRE0wTlY4U0JtVnpMVFF4T1NnQVAB'}, #no arrojo resultados
                  'MX': {'name':'mexico', 'gl_language_id': 'es-419', 'newspapers': mexico_periodicos,
                        'topic_id':'CAAqKAgKIiJDQkFTRXdvSkwyMHZNR0k1TUY5eUVnWmxjeTAwTVRrb0FBUAE'},
                  'NI': {'name':'nicaragua', 'gl_language_id': 'es-419', 'newspapers': nicaragua_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZqTnpRU0JtVnpMVFF4T1NnQVAB'},
                  'PE': {'name':'peru', 'gl_language_id': 'es-419', 'newspapers': peru_periodicos,
                        'topic_id':'CAAqKAgKIiJDQkFTRXdvSkwyMHZNREUyZDNwM0VnWmxjeTAwTVRrb0FBUAE'},
                  'UY': {'name':'uruguay', 'gl_language_id': 'es-419', 'newspapers': uruguay_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRGQwZDNvU0JtVnpMVFF4T1NnQVAB'},
                  'PR': {'name':'puertorico', 'gl_language_id': 'es-419', 'newspapers': puerto_rico_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZ5TjNRU0JtVnpMVFF4T1NnQVAB'},
                  'PY': {'name':'paraguay', 'gl_language_id': 'es-419', 'newspapers': paraguay_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFYyTVRBU0JtVnpMVFF4T1NnQVAB'},
                  'BZ': {'name':'belice', 'gl_language_id': 'en', 'newspapers': belice_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREUyTkdJU0JtVnpMVFF4T1NnQVAB'},
                  'BB': {'name':'barbados', 'gl_language_id': 'en', 'newspapers': barbados_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREUyTW5ZU0JtVnpMVFF4T1NnQVAB'},
                  'TT': {'name':'trinidadytobago', 'gl_language_id': 'en', 'newspapers': trinidad_y_tobago_periodicos,
                        'topic_id':'CAAqKAgKIiJDQkFTRXdvSkwyMHZNRGxzZUhSbkVnWmxjeTAwTVRrb0FBUAE'},
                  'JM': {'name':'jamaica', 'gl_language_id': 'en', 'newspapers': jamaica_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRE5mY2pNU0JtVnpMVFF4T1NnQVAB'},
                  'SR': {'name':'suriname', 'gl_language_id': 'nl', 'newspapers': suriname_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1Ym1vU0JtVnpMVFF4T1NnQVAB'},
                  'VE': {'name':'venezuela', 'gl_language_id': 'es-419', 'newspapers': venezuela_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRGQ1YkdvU0JtVnpMVFF4T1NnQVAB'},
                  'PA': {'name':'panama', 'gl_language_id': 'es-419', 'newspapers': panama_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZ4ZURFU0JtVnpMVFF4T1NnQVAB'},
                  'GF': {'name':'guayanafrancesa', 'gl_language_id': 'fr', 'newspapers': guayana_francesa_periodicos,
                        'topic_id':'CAAqJggKIiBDQkFTRWdvSUwyMHZNREo0TWpFU0JtVnpMVFF4T1NnQVAB'},
                  }
