import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino as rh




viste = rs.ViewNames()
for viewport in viste:
    rs.ViewDisplayMode(viewport,"Shaded")
diametro = 1
brep =  rs.GetObjects("dammi un solido",16)
brepexp = rs.ExplodePolysurfaces(brep)
surface = rs.GetObject("dammi la superficie",8)
surf_edge = rs.DuplicateSurfaceBorder(surface,1)

new_surface = rs.CopyObject(surface,(0,0,0))
uv= []
temp_edge = rs.ExplodeCurves(surf_edge,False)

list_evpt =[]
for i in temp_edge:
    evpt =rs.CurveMidPoint(i)
    print evpt
    list_evpt.append(evpt)
for i in list_evpt:
    bord= rs.SurfaceClosestPoint(new_surface,i)
    uv.append(bord)
for i in uv:
    rs.ExtendSurface(new_surface,i,diametro*10)
edge = rs.OffsetCurveOnSurface(surf_edge,new_surface,-diametro)
print edge
if rs.CurveLength(edge)<rs.CurveLength(surf_edge):
    rs.DeleteObject(edge)
    edge =  rs.OffsetCurveOnSurface(surf_edge,new_surface,diametro)
surf_edge = rs.ExplodeCurves(surf_edge,True)
print edge

rs.ObjectColor(edge,(0,0,255))
for i in brepexp:
    rs.DeleteObject(i)
for i in temp_edge:
    rs.DeleteObject(i)
for i in surf_edge:
    rs.DeleteObject(i)

rs.DeleteObjects([new_surface,surface])
