def castorlayout(i, p, *rows):
    i["Castor/Layouts/" + p] = DQMItem(layout=rows)


castorlayout(dqmitems, "01 - Map of frontend and readout errors",
           [{ 'path': "Castor/CastorDigiMonitor/CASTOR QIE_capID+er+dv",
             'description':"Frontend and readout errors"}]
           )

castorlayout(dqmitems, "02 - Channel-wise timing",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(x=Tile y=TS) (cumulative)",
             'description':"Channel-wise timing"}]
           )
castorlayout(dqmitems, "02b - Channel-wise timing (rms)",
           [{ 'path': "Castor/CastorDigiMonitor/QrmsfC=f(Tile TS)",
             'description':"Channel-wise timing (rms)"}]
           )

castorlayout(dqmitems, "03 - CASTOR DeadChannelsMap",
           [{ 'path': "Castor/CastorDigiMonitor/CASTOR DeadChannelsMap",
             'description':"CASTOR DeadChannelsMap"}]
           )

castorlayout(dqmitems, "04 - DigiSize",
           [{ 'path': "Castor/CastorDigiMonitor/DigiSize",
             'description':"CASTOR DigiSize",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "05 - CASTOR Tower Depth",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORTowerDepth",
             'description':"CASTORTowerDepth"}]
           )

castorlayout(dqmitems, "06 - Tower EM vs HAD",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORTowerEMvsEhad",
             'description':"CASTOR Tower EM vs Ehad",
 'draw': { 'xtype': 'log', 'ytype':'log', 'drawopts': "COLZ" } }]
           )

