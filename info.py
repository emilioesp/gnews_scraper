'''
countries codes source: http://www.genealogyintime.com/articles/country-guide-to-google-search-engines-page3.html
languages codes source: https://docs.appmanager.io/docs/list-of-supported-languages-and-locale-codes
'''

#Periodicos
argentina_periodicos = ['www.clarin.com', 'www.lanacion.com.ar', 'www.pagina12.com.ar',
             'www.tiempoar.com.ar', 'www.diariopopular.com.ar',
             'www.cronica.com.ar', 'www.laprensa.com.ar', 'www.ole.com.ar',
             'www.ambito.com', 'www.cronista.com', 'www.baenegocios.com',
             'www.eleconomista.com.ar']
argentina_periodicos = argentina_periodicos + [x.replace('www.','') for x in argentina_periodicos]

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
brasil_periodicos = brasil_periodicos + [x.replace('www.','') for x in brasil_periodicos]

chile_periodicos = ['www.latercera.com', 'www.emol.com', 'www.lun.com', 'www.lacuarta.com',
         'www.lasegunda.com', 'www.publimetro.cl', 'www.lahora.cl',
         'www.hoyxhoy.cl', 'www.elgraficochile.cl', 'www.df.cl', 'www.pulso.cl']
chile_periodicos = chile_periodicos + [x.replace('www.','') for x in chile_periodicos]

ecuador_periodicos = ['www.lahora.com.ec', 'www.elcomercio.com', 'www.ultimasnoticias.ec',
           'www.metroecuador.com.ec', 'www.primicias.ec', 'www.cerolatitud.ec']
ecuador_periodicos = ecuador_periodicos + [x.replace('www.','') for x in ecuador_periodicos]

peru_periodicos = ['www.larepublica.pe', 'www.elcomercio.pe', 'www.diariocorreo.pe',
        'www.peru21.pe', 'www.larazon.pe', 'www.laprimera.pe',
        'www.expreso.com.pe', 'www.elperuano.pe', 'www.delpais.com.pe',
        'www.elperfil.pe', 'www.exitosanoticias.pe', 'www.trome.pe',
        'www.ojo.pe', 'www.elpopular.pe', 'www.extra.com.pe',
        'www.elchino.pe', 'www.elmen.pe', 'www.radiokaribena.pe',
        'www.diarionuevosol.com', 'www.diariouno.pe', 'www.lanacionperu.com',
        'www.publimetro.pe', 'www.libero.pe', 'www.depor.com',
        'www.elbocon.pe', 'www.todosport.pe', 'www.gestion.pe',
        'www.perushimpo.com', 'www.lapatria.pe', 'www.cronicaviva.com.pe',
        'www.peruinforma.com', 'www.dsn.pe', 'www.andina.pe', 'www.laprensa.pe']
peru_periodicos = peru_periodicos + [x.replace('www.','') for x in peru_periodicos]

guatemala_periodicos = ['www.prensalibre.com', 'www.lahora.gt', 'www.elperiodico.com.gt',
             'www.dca.gob.gt', 'www.nuestrodiario.com', 'www.aldia.com.gt',
             'www.publinews.gt', 'www.soy502.com', 'www.nomada.gt',
             'www.republica.gt', 'www.guatemala.com', 'www.newsinamerica.com',
             'www.ojoconmipisto.com', 'www.perspectiva.gt',
             'www.elmetropolitano.com.gt']
guatemala_periodicos = guatemala_periodicos + [x.replace('www.','') for x in guatemala_periodicos]

el_salvador_periodicos = ['www.elsalvador.com', 'www.laprensagrafica.com', 'www.elmundo.sv',
               'www.diariocolatino.com', 'www.elgrafico.com', 'www.lapagina.com.sv',
               'www.elsalvadortimes.com', 'www.elfaro.net', 'www.contrapunto.com.sv',
               'www.solonoticias.com', 'www.ultimahora.sv', 'www.verdaddigital.com',
               'www.diariolahuella.com', 'www.elindependiente.sv', 'www.elurbano.news']
el_salvador_periodicos = el_salvador_periodicos + [x.replace('www.','') for x in el_salvador_periodicos]

honduras_periodicos = ['www.latribuna.hn', 'www.elheraldo.hn', 'www.diez.hn',
            'www.diariomas.hn', 'www.proceso.hn', 'www.hondudiario.com',
            'www.tiempo.hn', 'www.ellibertador.hn', 'www.confidencialhn.com',
            'www.enaltavoz.com', 'www.elsoldehonduras.com',
            'www.libertaddigital.news', 'www.criterio.hn', 'www.elmundo.hn',
            'www.paradigma.hn', 'www.quienopina.com', 'www.dinero.hn']
honduras_periodicos = honduras_periodicos + [x.replace('www.','') for x in honduras_periodicos]

colombia_periodicos = ['www.eltiempo.com', 'www.publimetro.co', 'www.elespectador.com',
            'www.elnuevosiglo.com.co', 'www.qhubo.com', 'www.diarioadn.co',
            'www.larepublica.co', 'www.portafolio.co']
colombia_periodicos = colombia_periodicos + [x.replace('www.','') for x in colombia_periodicos]

mexico_periodicos = ['www.milenio.com', 'www.excelsior.com.mx', 'www.eluniversal.com.mx',
          'www.heraldodemexico.com.mx', 'www.reforma.com',
          'www.publimetro.com.mx', 'www.la-prensa.com.mx', 'www.elgrafico.mx',
          'www.capitalmexico.com.mx', 'www.jornada.unam.mx',
          'www.unomasuno.com.mx', 'www.cronica.com.mx', 'www.razon.com.mx',
          'www.impacto.mx', 'www.elsoldemexico.com.mx', 'www.diariodemexico.com',
          'www.contrareplica.mx', 'www.diariobasta.com', 'www.elpuntocritico.com',
          'www.periodicoeldia.mx', 'www.reporteindigo.com', 'www.elnovedades.com',
          'www.miled.com', 'www.pasala.com.mx', 'www.thenews.mx',
          'www.maspormas.com.mx', 'www.24-horas.mx', 'www.record.com.mx',
          'www.esto.com.mx', 'www.ovaciones.com', 'www.estadiodeportes.mx',
          'www.cancha.com', 'www.elfinanciero.com.mx', 'www.eleconomista.com.mx']
mexico_periodicos = mexico_periodicos + [x.replace('www.','') for x in mexico_periodicos]


countries_info = {
                  'AR': {'name':'argentina', 'gl_language_id': 'es-419', 'newspapers': argentina_periodicos},
                  'BR': {'name':'brasil', 'gl_language_id': 'pt-BR', 'newspapers': brasil_periodicos},
                  'CL': {'name':'chile', 'gl_language_id': 'es-419', 'newspapers': chile_periodicos},
                  'CO': {'name':'colombia', 'gl_language_id': 'es-419', 'newspapers': colombia_periodicos},
                  'HN': {'name':'honduras', 'gl_language_id': 'es-419', 'newspapers': honduras_periodicos},
                  'EC': {'name':'ecuador', 'gl_language_id': 'es-419', 'newspapers': ecuador_periodicos},
                  'SV': {'name':'elsalvador', 'gl_language_id': 'es-419', 'newspapers': el_salvador_periodicos},
                  'GT': {'name':'guatemala', 'gl_language_id': 'es-419', 'newspapers': guatemala_periodicos},
                  'MX': {'name':'mexico', 'gl_language_id': 'es-419', 'newspapers': mexico_periodicos},
                  'PE': {'name':'peru', 'gl_language_id': 'es-419', 'newspapers': peru_periodicos},
                  }
