import rhinoscriptsyntax as rs
import Rhino as rh

rs.Command("_SelPt")
rs.Command("_Delete")
c1 = 0
c2 = 0
val = 30
valSicurezza = 50
curve = rs.GetObject("dammi una curva")
fori= rs.GetObject("dammi i fori")
pinza = rs.GetObject("dammi la pinza")
if rs.IsCurve(curve) and rs.IsCurve(fori) and rs.IsCurve(pinza):
    print "curva ottenuta"
    point = rs.BoundingBox(curve)
    px = point[0].X
    py = point[0].Y
    rs.AddPoint(px,py)
    while (px<point[2].X):
        oldpy = py
        py = point[0].Y
        c2 = 0
        if c1 == val:
            break
        while (py<point[2].Y):
#            if rs.PointInPlanarClosedCurve([px,py],curve) and not rs.PointInPlanarClosedCurve([px,py],fori):
#                puntofinale =rs.AddPoint(px,py)
#                originepinza = rs.AddPoint(oldpx,oldpy)
#                pinzaorientata = rs.CopyObject(pinza,rs.VectorCreate(originepinza,puntofinale))
#                print "successo"
#                print originepinza
            if rh.Geometry.Intersect.Intersection.CurveCurve(rs.coercecurve(pinza),rs.coercecurve(fori),0.1,0.1):
                print "true"
            if not rs.PointInPlanarClosedCurve((px,py),fori) and rs.PointInPlanarClosedCurve((px,py),curve):
                rs.AddPoint(px,py)
            c2= c2+1
            py = py +val
            print [c1,c2]

#        originepinza = rs.CurveAreaCentroid(pinza)
#        rs.OrientObject(pinza,originepinza,[px,py])
        px = px + val
        c1 = c1+1

else:
    print "errore"
    
    
