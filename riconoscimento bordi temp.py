import rhinoscriptsyntax as rs
import Rhino as rh

rs.Command("_SelPt")
rs.Command("_Delete")
c1 = 0
c2 = 0
val = 30
valSicurezza = 50
curve = rs.GetObject("dammi una curva")
fori= rs.GetObjects("dammi i fori")
boolfori = True
for i in fori:
    if boolfori == rs.IsCurve(fori[1]):
        boolfori = True
    else:
        boolfori = False
        break
    
    
if rs.IsCurve(curve) and boolfori:
    print "curva ottenuta"
    print  boolfori
    puntidarimuovere = []
    point = rs.BoundingBox(curve)
    px = point[0].X
    py = point[0].Y
    while (px<point[2].X):
        oldpy = py
        py = point[0].Y
        c2 = 0
        if c1 == val:
            break
        while (py<point[2].Y):
            if rs.PointInPlanarClosedCurve((px,py),curve):
                for i in fori:
                    print "fori"
                    if rs.PointInPlanarClosedCurve((px,py),i):
                        punto = rs.AddPoint(px,py)
                        break
            c2= c2+1
            py = py +val
            print [c1,c2]
            if c2>valSicurezza:
                break
        px = px + val
        c1 = c1+1

else:
    print "errore"
    