def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def comuna_sinacentos(s):
    replacements=(
        ('curaco de velez','curaco de vélez'),
        ('constitucion','constitución'),
        ('combarbala','combarbalá'),
        ('juan fernandez','juan fernández'),
        ('puchuncavi','puchuncaví'),
        ('santa maria','santa maría'),
        ('alto biobio','alto biobío'),
        ('san nicolas','san nicolás'),
        ('san joaquin','san joaquín'),
        ('concepcion','concepción'),
        ('san fabian','san fabián'),
        ('pitrufquen','pitrufquén'),
        ('curacautin','curacautín'),
        ('futaleufu','futaleufú'),
        ('hualaihue','hualaihué'),
        ('rio ibañez','río ibáñez'),
        ('rio ibáñez','río ibáñez'),
        ('río ibañez','río ibáñez'),
        ('valparaiso','valparaíso'),
        ('vichuquen','vichuquén'),
        ('santa barbara','santa bárbara'),
        ('puqueldon','puqueldón'),
        ('conchali','conchalí'),
        ('peñalolen','peñalolén'),
        ('san ramon','san ramón'),
        ('san jose de maipo','san josé de maipo'),
        ('curacavi','curacaví'),
        ('copiapo','copiapó'),
        ('quilpue','quilpué'),
        ('machali','machalí'),
        ('hualañe','hualañé'),
        ('licanten','licantén'),
        ('longavi','longaví'),
        ('traiguen','traiguén'),
        ('la union','la unión'),
        ('cochamo','cochamó'),
        ('estacion central','estación central'),
        ('ollague','ollagüe'),
        ('curico','curicó'),
        ('hualpen','hualpén'),
        ('mulchen','mulchén'),
        ('chillan','chillán'),
        ('chillan viejo','chillán viejo'),
        ('quillon','quillón'),
        ('maullin','maullín'),
        ('queilen','queilén'),
        ('quellon','quellón'),
        ('chaiten','chaitén'),
        ('concon','concón'),
        ('olmue','olmué'),
        ('requinoa','requínoa'),
        ('colbun','colbún'),
        ('ñiquen','ñiquén'),
        ('tolten','toltén'),
        ('vilcun','vilcún'),
        ('maipu','maipú'),
        ('alhue','alhué'),
        ('maria elena','maría elena'),
        ('tome','tomé'),
        ('tirua','tirúa'),
        ('pucon','pucón'),
        ('puren','purén'),
        ('aisen','aisén'),
        ('antartica','antártica'),
        ('maria pinto','maría pinto'),
        ('chepica','chépica'),
        ('rio hurtado','río hurtado'),
        ('rio claro','río claro'),
        ('ranquil','ránquil'),
        ('mafil','máfil'),
        ('rio bueno','río bueno'),
        ('rio negro','río negro'),
        ('rio verde','río verde'),
    )
    s= s.lower()
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b)
    return s
