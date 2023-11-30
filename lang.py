LANGUAGES = {'en', 'fr', 'it', 'de', 'es'}
button_text = {'en': 'Send Location', 'it': 'Invia la posizione', 'de': 'Standort senden', 'fr': 'Envoyer l\'emplacement', 'es': 'Enviar ubicación'}
start_message = {
    'en': ("🚨<b>FIND THE NEAREST DAE AROUND YOU</b>\n"
           "This bot will help you find the nearest defibrillator around you (1km area) thanks to the data saved in OpenStreetMap.\n\n"
           "Click the button below and authorize location access to find the nearest defibrillator."),
    'it': ("🚨<b>TROVA IL DAE PIU' VICINO A TE</b>\n"
           "Questo bot ti aiuterà a rintracciare il defibrillatore più vicino a te (in un'area di 1 km) grazie ai dati salvati in OpenStreetMap.\n\n"
           "Clicca il pulsante sottostante e autorizza l'accesso alla posizione per trovare il defibrillatore più vicino."),
    'de': ("🚨<b>FINDE DEN NÄCHSTEN DAE IN DEINER NÄHE</b>\n"
           "Dieser Bot wird dir helfen, den nächstgelegenen Defibrillator in deiner Umgebung (1 km Bereich) mithilfe der in OpenStreetMap gespeicherten Daten zu finden.\n\n"
           "Klicke auf den unten stehenden Button und erlaube den Zugriff auf deinen Standort, um den nächstgelegenen Defibrillator zu finden."),
    'fr': ("🚨<b>TROUVEZ LE DAE LE PLUS PROCHE DE VOUS</b>\n"
           "Ce bot vous aidera à localiser le défibrillateur le plus proche de vous (dans un rayon de 1 km) grâce aux données enregistrées dans OpenStreetMap.\n\n"
           "Cliquez sur le bouton ci-dessous et autorisez l'accès à l'emplacement pour trouver le défibrillateur le plus proche."),
    'es': ("🚨<b>ENCUENTRA EL DAE MÁS CERCANO A TI</b>\n"
           "Este bot te ayudará a encontrar el desfibrilador más cercano a ti (área de 1 km) gracias a los datos guardados en OpenStreetMap.\n\n"
           "Haz clic en el botón de abajo y autoriza el acceso a la ubicación para encontrar el desfibrilador más cercano.")
}
response_init = {'en': "🚨 <b>NEAREST DEFIBRILLATORS:</b>\n",
                 'it': "🚨 <b>DEFIBRILLATORI PIÙ VICINI:</b>\n",
                 'de': "🚨 <b>NÄCHSTGELEGENE DEFIBRILLATOREN:</b>\n",
                 'fr': "🚨 <b>DÉFIBRILLATEURS LES PLUS PROCHE :</b>\n",
                 'es': "🚨 <b>DESFIBRILADORES MÁS CERCANOS:</b>\n"}
response_not_found = {'en': "\nNo defibrillators found.\n",
                      'it': "\nNessun defibrillatore trovato.\n",
                      'de': "\nKeine Defibrillatoren gefunden.\n",
                      'fr': "\nAucun défibrillateur trouvé.\n",
                      'es': "\nNo se encontraron desfibriladores.\n"}
response_found = {'en': "Click on the button to get directions.",
                  'it': "Clicca sul pulsante per ottenere le indicazioni.",
                  'de': "Klicke auf den Button, um Wegbeschreibungen zu erhalten.",
                  'fr': "Cliquez sur le bouton pour obtenir des indications.",
                  'es': "Haz clic en el botón para obtener indicaciones."}
report_button = {
    'en': "Report a missing defibrillator",
    'it': "Segnala un defibrillatore mancante",
    'de': "Melden Sie einen fehlenden Defibrillator",
    'fr': "Signaler un défibrillateur manquant",
    'es': "Informar de un desfibrilador faltante"
}
report_message = {
    'en': ("📝<b>REPORT A MISSING DEFIBRILLATOR</b>\n"
           "Using exclusively the data available on OpenStreetMap, it's possible that some AEDs may not be present on the map.\n"
           "If you have found a public defibrillator not indicated on the map, click the button below and provide as many details as possible.\n\n"
           "Useful details:\n"
           "-Address and/or GPS coordinates\n-Photos indicating its location\n-Additional notes\n\n"
           "Your report will be considered, and the AED will be added to the map as soon as possible.\n"
           "Thank you for your contribution!❤️"),
    'it': ("📝<b>SEGNALA UN DEFIBRILLATORE MANCANTE</b>\n"
           "Utilizzando esclusivamente i dati presenti su OpenStreetMap è possibile che alcuni DAE non siano stati presenti sulla mappa.\n"
           "Se hai trovato un defibrillatore pubblico non indicato sulla mappa, clicca il pulsante qua sotto e indica più dettagli possibili.\n\n"
           "Dettagli utili:\n"
           "-Indirizzo e o coordinate GPS\n-Foto che indicano la sua posizione\n-Note aggiuntive\n\n"
           "La tua segnalazione sarà presa in considerazione e il DAE verrà aggiunto alla mappa il prima possibile.\n"
           "Grazie per il tuo contributo!❤️"),
    'de': ("📝<b>MELDE EINEN FEHLENDEN DEFIBRILLATOR</b>\n"
           "Es ist möglich, dass einige Defibrillatoren aufgrund der ausschließlichen Verwendung der auf OpenStreetMap verfügbaren Daten nicht auf der Karte verzeichnet sind.\n"
           "Wenn du einen öffentlichen Defibrillator gefunden hast, der nicht auf der Karte verzeichnet ist, klicke auf den unten stehenden Button und gib so viele Details wie möglich an.\n\n"
           "Nützliche Details:\n"
           "-Adresse und/oder GPS-Koordinaten\n-Fotos, die seinen Standort anzeigen\n-Zusätzliche Hinweise\n\n"
           "Deine Meldung wird berücksichtigt und der Defibrillator wird so schnell wie möglich zur Karte hinzugefügt.\n"
           "Vielen Dank für deinen Beitrag!❤️"),
    'fr': ("📝<b>SIGNALER UN DÉFIBRILLATEUR MANQUANT</b>\n"
           "En utilisant exclusivement les données disponibles sur OpenStreetMap, il est possible que certains DAE ne soient pas présents sur la carte.\n"
           "Si vous avez trouvé un défibrillateur public non indiqué sur la carte, cliquez sur le bouton ci-dessous et fournissez autant de détails que possible.\n\n"
           "Détails utiles :\n"
           "-Adresse et/ou coordonnées GPS\n-Photos indiquant son emplacement\n-Notes supplémentaires\n\n"
           "Votre signalement sera pris en compte et le DAE sera ajouté à la carte dès que possible.\n"
           "Merci pour votre contribution!❤️"),
    'es': ("📝<b>INFORMAR DE UN DESFIBRILADOR FALTANTE</b>\n"
           "Utilizando exclusivamente los datos disponibles en OpenStreetMap, es posible que algunos DEA no estén presentes en el mapa.\n"
           "Si has encontrado un desfibrilador público no indicado en el mapa, haz clic en el botón de abajo y proporciona tantos detalles como sea posible.\n\n"
           "Detalles útiles:\n"
           "-Dirección y/o coordenadas GPS\n-Fotos que indiquen su ubicación\n-Notas adicionales\n\n"
           "Tu informe será considerado y el desfibrilador se añadirá al mapa lo antes posible.\n"
           "¡Gracias por tu contribución!❤️")
}
help_message = {
    'en': ("ℹ<b>INFORMATION</b>\n"
           "This bot was created to help you find the nearest defibrillators to you.\n"
           "The bot uses data from OpenStreetMap, a collaborative project to create free, editable maps. Therefore, it's possible that some defibrillators may not be present on the map.\n"
           "We are continuously working to gather as much data as possible to update the map and make this bot as useful and reliable as possible.\n"
           "If you want to contribute to the project by reporting a missing defibrillator, type /report in the chat and follow the instructions.\n\n"
           "Available commands:\n"
           "- /start: start the bot\n- /report: report a missing defibrillator\n- /help: show this message\n\n"
           "For more information about the project, contact <a href='mailto:damiano@nicolussi.dev' target='_blank'>damiano@nicolussi.dev</a>\n"
           "The website is currently under construction, but you can find the source code on GitHub"),
    'it': ("ℹ<b>INFORMAZIONI</b>\n"
           "Questo bot è stato creato per aiutare a trovare i defibrillatori più vicini a te.\n"
           "Il bot utilizza i dati presenti su OpenStreetMap, un progetto collaborativo per creare mappe libere ed editabili, è dunque possibile che alcuni defibrillatori non siano presenti sulla mappa.\n"
           "Siamo comunque al lavoro per recuperare il maggior numero di dati possibile per aggiornare la mappa e rendere questo bot il più utile e attendibile possibile.\n"
           "Se vuoi contribuire al progetto segnalando un defibrillatore mancante, digita /report in chat e segui le istruzioni.\n\n"
           "I comandi disponibili sono:\n"
           "- /start: avvia il bot\n- /report: segnala un defibrillatore mancante\n- /help: mostra questo messaggio\n\n"
           "Per scoprire più informazioni sul progetto, contatta <a href='mailto:damiano@nicolussi.dev' target='_blank'>damiano@nicolussi.dev</a>\n"
           "Il Sito Web è attualmente in costruzione, ma puoi trovare il codice sorgente su GitHub"),
    'de': ("ℹ<b>INFORMATION</b>\n"
           "Dieser Bot wurde erstellt, um Ihnen bei der Suche nach den nächstgelegenen Defibrillatoren zu helfen.\n"
           "Der Bot verwendet Daten von OpenStreetMap, einem gemeinschaftlichen Projekt zur Erstellung von kostenlosen, bearbeitbaren Karten. Daher ist es möglich, dass einige Defibrillatoren auf der Karte nicht verzeichnet sind.\n"
           "Wir arbeiten kontinuierlich daran, so viele Daten wie möglich zu sammeln, um die Karte zu aktualisieren und diesen Bot so nützlich und zuverlässig wie möglich zu machen.\n"
           "Wenn Sie zum Projekt beitragen möchten, indem Sie einen fehlenden Defibrillator melden, geben Sie /report im Chat ein und folgen Sie den Anweisungen.\n\n"
           "Verfügbare Befehle:\n"
           "- /start: startet den Bot\n- /report: meldet einen fehlenden Defibrillator\n- /help: zeigt diese Nachricht an\n\n"
           "Für weitere Informationen zum Projekt kontaktieren Sie <a href='mailto:damiano@nicolussi.dev' target='_blank'>damiano@nicolussi.dev</a>\n"
           "Die Website ist derzeit im Aufbau, aber Sie können den Quellcode auf GitHub finden"),
    'fr': ("ℹ<b>INFORMATIONS</b>\n"
           "Ce bot a été créé pour vous aider à trouver les défibrillateurs les plus proches de vous.\n"
           "Le bot utilise des données provenant d'OpenStreetMap, un projet collaboratif visant à créer des cartes libres et modifiables. Il est donc possible que certains défibrillateurs ne soient pas présents sur la carte.\n"
           "Nous travaillons constamment à rassembler autant de données que possible pour mettre à jour la carte et rendre ce bot aussi utile et fiable que possible.\n"
           "Si vous souhaitez contribuer au projet en signalant un défibrillateur manquant, tapez /report dans le chat et suivez les instructions.\n\n"
           "Commandes disponibles :\n"
           "- /start : démarre le bot\n- /report : signale un défibrillateur manquant\n- /help : affiche ce message\n\n"
           "Pour plus d'informations sur le projet, contactez <a href='mailto:damiano@nicolussi.dev' target='_blank'>damiano@nicolussi.dev</a>\n"
           "Le site web est actuellement en construction, mais vous pouvez trouver le code source sur GitHub"),
    'es': ("ℹ<b>INFORMACIÓN</b>\n"
           "Este bot fue creado para ayudarte a encontrar los desfibriladores más cercanos a ti.\n"
           "El bot utiliza datos de OpenStreetMap, un proyecto colaborativo para crear mapas libres y editables. Por lo tanto, es posible que algunos desfibriladores no estén presentes en el mapa.\n"
           "Estamos trabajando continuamente para recopilar la mayor cantidad de datos posible para actualizar el mapa y hacer que este bot sea lo más útil y confiable posible.\n"
           "Si deseas contribuir al proyecto informando de un desfibrilador que falta, escribe /report en el chat y sigue las instrucciones.\n\n"
           "Comandos disponibles:\n"
           "- /start: inicia el bot\n- /report: informa de un desfibrilador que falta\n- /help: muestra este mensaje\n\n"
           "Para obtener más información sobre el proyecto, comunícate con <a href='mailto:damiano@nicolussi.dev' target='_blank'>damiano@nicolussi.dev</a>\n"
           "El sitio web está actualmente en construcción, pero puedes encontrar el código fuente en GitHub")
}