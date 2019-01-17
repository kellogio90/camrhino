import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino as rh


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


viste = rs.ViewNames()
for viewport in viste:
    rs.ViewDisplayMode(viewport,"Shaded")
diametro = rs.StringBox("dimensione della punta","10","scontornatura")
if RepresentsInt(diametro):
    diametro = int(diametro)
else:
    diametro = 10
brep =  rs.GetObjects("dammi un solido",16)
brepexp = rs.ExplodePolysurfaces(brep)
get_val = rs.GetEdgeCurves("dammi le curve")
surf_edge = []

for i in get_val:
    surf_edge.append(i[0])
    surface = rs.SelectObject(i[1])
surf_edge = rs.coerceguidlist(surf_edge)
surf_edge = rs.JoinCurves(surf_edge,True)
surf_edge = surf_edge[0]
surface = rs.GetObjects("conferma la selezione",8,False,True,surface,1,1)

print surf_edge
uv= []
temp_edge = rs.ExplodeCurves(surf_edge,False)
new_surface = rs.CopyObject(surface,(0,0,0))
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
