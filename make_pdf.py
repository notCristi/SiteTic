# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

BROWN = HexColor("#7a2e12")
GREY = HexColor("#555555")

styles = getSampleStyleSheet()
title = ParagraphStyle("title", parent=styles["Title"], fontName="Times-Bold",
                       fontSize=22, textColor=BROWN, spaceAfter=2, alignment=TA_CENTER)
sub = ParagraphStyle("sub", parent=styles["Normal"], fontName="Times-Italic",
                     fontSize=13, textColor=GREY, alignment=TA_CENTER, spaceAfter=4)
cast = ParagraphStyle("cast", parent=styles["Normal"], fontName="Times-Roman",
                      fontSize=10.5, textColor=HexColor("#444444"), alignment=TA_CENTER, spaceAfter=16)
akt = ParagraphStyle("akt", parent=styles["Normal"], fontName="Times-Bold",
                     fontSize=13, textColor=BROWN, spaceBefore=14, spaceAfter=6)
scene = ParagraphStyle("scene", parent=styles["Normal"], fontName="Times-Italic",
                       fontSize=11, textColor=GREY, spaceBefore=8, spaceAfter=8, alignment=TA_JUSTIFY)
line = ParagraphStyle("line", parent=styles["Normal"], fontName="Times-Roman",
                      fontSize=12.5, leading=18, alignment=TA_JUSTIFY, spaceAfter=8)

def N(name):
    return '<font color="#7a2e12"><b>%s:</b></font>' % name
def S(t):  # stage direction
    return '<font color="#666666"><i>%s</i></font>' % t

doc = SimpleDocTemplate("/home/user/SiteTic/Warenwelt_Piratenhut.pdf", pagesize=A4,
                        leftMargin=2.2*cm, rightMargin=2.2*cm,
                        topMargin=2.0*cm, bottomMargin=2.0*cm,
                        title="Die Piratenhut-Schlacht")

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=HexColor("#c9aa99"),
                      spaceBefore=10, spaceAfter=10)

E = []
E.append(Paragraph("Die Piratenhut-Schlacht", title))
E.append(Paragraph("Ein Sketch aus der Warenwelt", sub))
E.append(Paragraph("<b>Personen:</b> Maia (Verkäuferin am Flohmarkt) &middot; Bea (Verkäuferin im Fachgeschäft) &middot; Dumi (Kunde) &middot; Vlad (Kunde)", cast))
E.append(hr())

E.append(Paragraph(S("Ein Marktplatz. Links steht der bunte Flohmarktstand von MAIA, vollgestopft mit alten Schätzen. Rechts glänzt das edle Fachgeschäft von BEA, alles neu und teuer. DUMI und VLAD schlendern herein."), scene))

E.append(Paragraph("1. AKT &ndash; DIE RIVALITÄT", akt))

E.append(Paragraph(N("MAIA") + " Willkommen, willkommen in der echten Warenwelt! Hier am Flohmarkt findet ihr Geschichte zum Anfassen! Jede Tasse, jede Lampe, jeder Löffel hat schon gelebt, geliebt, gelitten! Bei mir kauft ihr nicht einfach Dinge &ndash; ihr kauft Abenteuer! Diese Vase hier? Hundert Jahre alt! Dieser Stuhl? Auf ihm hat angeblich ein Graf geschlafen! Und das Beste: alles zum kleinen Preis. Kommt her, kommt näher, fasst an, träumt! Drüben bei der feinen Dame zahlt ihr nur für die Verpackung und das hochnäsige Lächeln. Hier bei Maia zahlt ihr für die Seele der Dinge! " + S("(wischt stolz über einen verstaubten Krug)") + " Sehen Sie diesen Glanz? Das ist gelebte Patina, meine Herren, kein billiger Lack! Und falls etwas wackelt &ndash; das nennt man Charakter! Ein Gegenstand ohne Geschichte ist wie eine Suppe ohne Salz. Langweilig! Tot! Drüben gibt es nur seelenlose Schachteln aus der Fabrik, alle gleich, alle kalt. Hier ist jedes Stück ein Unikat. Ein echtes Original! Also, meine Herren, wer von euch will heute ein Stück Ewigkeit mit nach Hause nehmen? Ich mache euch einen Preis, da weint die Konkurrenz!", line))

E.append(Paragraph(N("BEA") + " " + S("(empört, rückt ihre Brille zurecht)") + " Ewigkeit? Das ist Staub, liebe Maia, nichts als Staub! Meine Herren, kommen Sie herüber ins Fachgeschäft, wo die Dinge nicht riechen, sondern glänzen! Bei mir bekommen Sie Qualität, Garantie und &ndash; man stelle sich vor &ndash; Sauberkeit! Drüben kaufen Sie die Erkältung gleich gratis dazu. Hier ist alles neu, originalverpackt, geprüft und edel. Kein Graf hat darauf geschlafen, Gott sei Dank, denn ich weiß, wo meine Ware herkommt! Sehen Sie diese Eleganz? Das ist kein Zufall, das ist Niveau. Ein Mann von Geschmack kauft nicht im Trödel, er kauft im Fachgeschäft! Ich verkaufe keine Geschichten, ich verkaufe Wert. Eine Vase, die hält, ein Stuhl, der nicht zusammenbricht, sobald man sich setzt. " + S("(zeigt anklagend auf Maias Stand)") + " Charakter nennt sie das? Ich nenne es kaputt! Bei mir gibt es Beratung, Rechnung und ein Lächeln, das echt ist und nicht aufgemalt. Meine Herren, gönnen Sie sich das Beste. Sie haben es verdient. Treten Sie ein in die wahre Warenwelt &ndash; die saubere, die feine, die moderne. Maia kann ihre alten Krüge behalten. Ich biete Ihnen die Zukunft, hübsch verpackt und mit Schleife obendrauf.", line))

E.append(hr())
E.append(Paragraph("2. AKT &ndash; DER PIRATENHUT ERSCHEINT", akt))
E.append(Paragraph(S("DUMI entdeckt zwischen den Waren einen alten, prächtigen Piratenhut und hebt ihn hoch."), scene))

E.append(Paragraph(N("DUMI") + " " + S("(begeistert)") + " Halt, halt, was ist das denn? Vlad, schau dir das an! Ein Piratenhut! Ein echter, riesiger Piratenhut mit Feder und allem Drum und Dran! Den will ich haben. Den muss ich haben! Sofort! " + S("(setzt ihn auf, posiert)") + " Wie sehe ich aus? Wie ein Kapitän, oder? Wie der gefährlichste Seeräuber aller sieben Weltmeere! Damit gehe ich auf jede Party und alle drehen sich um. Niemand sonst hat so etwas, niemand! Vlad, fühl mal die Feder, ist die nicht herrlich? Also, meine Damen, ich frage ganz direkt: Was kostet dieser wunderbare Hut? Und sagen Sie mir bloß keinen Mondpreis, sonst gehe ich wieder. Aber ehrlich &ndash; ich bin verliebt. Dieser Hut und ich, wir gehören zusammen. Das ist Schicksal! " + S("(zu Vlad)") + " Sag mal, steht er mir nicht fantastisch? Sei ehrlich, aber nicht zu ehrlich! Ich sehe schon die Blicke der Leute. Der Mann mit dem Piratenhut! So werde ich genannt werden. Eine Legende! Also, wer von euch beiden verkauft mir dieses Prachtstück? Ich höre. Und ich warne euch: Ich vergleiche die Angebote ganz genau. Auf geht's, überzeugt mich!", line))

E.append(Paragraph(N("VLAD") + " " + S("(skeptisch, verschränkt die Arme)") + " Moment mal, Dumi, nicht so schnell! Einen Hut kauft man nicht mit dem Herzen, sondern mit dem Kopf. Lass mich das prüfen. " + S("(nimmt den Hut, dreht ihn um, beklopft ihn)") + " Hmm. Schwer. Verdächtig schwer. Und diese Feder &ndash; ist die überhaupt echt? Meine Herren Verkäuferinnen, ich bin ein vorsichtiger Mann. Ich falle nicht auf glänzende Versprechen herein. Ein Hut ist ein Hut. Wo kommt er her? Wer hat ihn getragen? Hat er Flöhe? " + S("(riecht daran, zuckt zurück)") + " Oje. Also, ich sage es offen: Bevor hier irgendjemand Geld ausgibt, will ich Argumente hören. Richtige Argumente! Nicht „er ist schön“, nicht „er ist alt“. Warum genau soll dieser Hut sein Geld wert sein? Dumi hier ist verliebt, der zahlt jeden Preis, der arme Kerl. Aber ich passe auf ihn auf. Ich bin sein Verstand, sozusagen. Also, liebe Maia, liebe Bea: Überzeugt mich! Erzählt mir, warum dieser eine Hut auf der ganzen Welt der beste ist. Und denkt daran &ndash; ich glaube nichts, was ich nicht dreimal gehört habe. Die Show kann beginnen. Wer fängt an? Aber bitte mit echten Verkaufsargumenten, nicht mit Theater!", line))

E.append(hr())
E.append(Paragraph("3. AKT &ndash; DER VERKAUFSKAMPF", akt))

E.append(Paragraph(N("MAIA") + " " + S("(reißt den Hut an sich, mit leuchtenden Augen)") + " Dieser Hut, meine Herren, ist kein gewöhnlicher Hut! Das ist der Hut von Kapitän Schwarzbart dem Schrecklichen! Mit diesem Hut hat er Stürme bezwungen, Schätze geborgen und mindestens drei Seeungeheuer besiegt! Spürt ihr nicht die Geschichte? Riecht ihr nicht das Salz der Meere? " + S("(hält ihn andächtig hoch)") + " Diese Feder stammt von einem Papagei, der einst auf seiner Schulter saß und Flüche brüllte! Jeder Kratzer erzählt von einer Schlacht, jeder Fleck von einem Abenteuer! Wer diesen Hut trägt, trägt die Seele eines echten Piraten! Drüben verkaufen sie tote Fabrikware &ndash; ich verkaufe Legenden! Stellt euch vor: Ihr betretet einen Raum mit diesem Hut, und alle flüstern: „Das ist er, der Mann mit der Seele eines Kapitäns!“ Kein Fachgeschäft der Welt kann euch das geben. Geschichte kann man nicht im Laden kaufen, meine Herren &ndash; nur hier, bei Maia, am echten Flohmarkt!", line))

E.append(Paragraph(N("BEA") + " " + S("(lacht spöttisch)") + " Kapitän Schwarzbart? Papagei? Ach, Maia, du und deine Märchen! Meine Herren, glauben Sie kein Wort. Dieser Hut ist kein altes Gerümpel &ndash; oder besser gesagt, bei mir wäre er es nicht! Hören Sie zu: Was ich Ihnen biete, ist ein zertifiziertes Sammlerstück! Limitierte Auflage, geprüfte Qualität, mit Echtheitszertifikat und edler Aufbewahrungsbox! Das ist kein verstaubter Flohmarktfund, das ist eine Investition! In zehn Jahren ist dieser Hut das Doppelte wert &ndash; vorausgesetzt, er ist sauber, gepflegt und ordentlich dokumentiert, so wie bei mir. Bei Maia bekommen Sie Flöhe und Phantasiegeschichten. Bei mir bekommen Sie einen echten Wert, der bleibt. Stellen Sie sich vor: in einer beleuchteten Vitrine, mit kleinem Schild: „Sammlerstück, Fachgeschäft Bea.“ Das ist Klasse! Das ist Niveau! Geschichten verblassen, meine Herren &ndash; Qualität bleibt für immer!", line))

E.append(hr())
E.append(Paragraph("4. AKT &ndash; DER RABATT-WAHNSINN", akt))

E.append(Paragraph(N("DUMI") + " " + S("(überfordert, dreht den Kopf hin und her)") + " Also gut, gut, ich bin überzeugt &ndash; von beiden! Aber jetzt zur wichtigsten Frage: Was kostet der Spaß? Vlad, halt mich fest, gleich nennen sie eine Zahl, bei der mir schlecht wird!", line))

E.append(Paragraph(N("MAIA") + " " + S("(schnell)") + " Für Sie, mein Herr, nur fünfzig Euro! Nein, warte &ndash; dreißig! Nein! Zehn! Ach, wissen Sie was? Nehmen Sie ihn geschenkt! Gratis! Umsonst! Und ich lege noch diese antike Taschenuhr dazu! Und einen Kaffee! Und meinen ewigen Respekt!", line))

E.append(Paragraph(N("BEA") + " " + S("(verzweifelt)") + " Geschenkt? Bei mir bekommen Sie ihn doppelt geschenkt! Sie nehmen den Hut, Sie nehmen das Zertifikat, die Box &ndash; und ich gebe Ihnen noch fünfzig Euro obendrauf, damit Sie ihn mitnehmen! Bitte! Und ein Sammlerstück Ihrer Wahl! Und ich trage die Tüte bis zu Ihnen nach Hause!", line))

E.append(Paragraph(N("VLAD") + " " + S("(grinst, hält beide Hände hoch)") + " Stopp, stopp, meine Damen! Atmen Sie durch, bevor Sie sich noch ruinieren! Wenn das so weitergeht, kaufen am Ende Sie uns etwas ab und danken sich noch dafür! Sehen Sie, genau darauf habe ich gewartet. Geduld, meine Damen, Geduld zahlt sich aus. Ein kluger Käufer rennt nie zur ersten Zahl &ndash; er wartet, bis der Preis von ganz allein nach unten fällt. Und was lernen wir daraus? Konkurrenz ist das schönste Geschenk für den Kunden! Solange ihr beide euch streitet, gewinnen immer wir. " + S("(zu Dumi)") + " Also, mein Freund, hör auf deinen Verstand: Du nimmst den Hut von Maia &ndash; wegen der Geschichte mit dem Kapitän und dem fluchenden Papagei. Und du nimmst das Zertifikat von Bea &ndash; wegen des Werts und der schicken Box. Und die fünfzig Euro nehmen wir natürlich auch, vielen herzlichen Dank! Den Kaffee bitte zum Mitnehmen, und die Taschenuhr auch gleich dazu. " + S("(setzt Dumi feierlich den Hut auf)") + " So! Jetzt bist du ein echter Kapitän mit Echtheitszertifikat, einer antiken Uhr und einem sauberen Gewinn von fünfzig Euro. Das, meine Damen, nenne ich ein gutes Geschäft &ndash; für uns!", line))

E.append(Paragraph(N("DUMI") + " " + S("(strahlt, posiert stolz mit dem Hut)") + " Arrr! Das, meine Damen, nenne ich die wahre Warenwelt! Zwei Geschäfte, ein einziger Hut &ndash; und am Ende verdiene ich auch noch Geld dabei! Seht mich an: der gefährlichste Kapitän, den dieser Markt je gesehen hat, und das völlig kostenlos! " + S("(klopft sich auf die Brust)") + " Mit Geschichte im Herzen und Zertifikat in der Tasche! Ich danke euch beiden von ganzem Herzen &ndash; ihr seid die besten Verkäuferinnen der Welt, jede auf ihre Weise. Die eine verkauft Träume, die andere verkauft Glanz, und ich, ich nehme einfach beides mit! " + S("(zu Maia und Bea, die sich böse anfunkeln)") + " Streitet ihr nur ruhig weiter, lasst euch von uns nicht stören. Wir kommen morgen ganz bestimmt wieder &ndash; und wer weiß, vielleicht gibt es dann sogar ein ganzes Piratenschiff geschenkt, mit Mannschaft und Papagei obendrauf! Komm, Vlad, setzen wir die Segel! Auf in die Warenwelt!", line))

E.append(Spacer(1, 14))
E.append(Paragraph(S("— ENDE —"), ParagraphStyle("end", parent=scene, alignment=TA_CENTER)))

doc.build(E)
print("PDF erstellt.")
