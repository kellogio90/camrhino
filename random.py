import rhinoscriptsyntax as rs  

def TestOffset():
    curve = rs.GetEdgeCurves("dammi le curve")
    if curve is None: return False
    
    crvs = [curve[n][0] for n in range(len(curve))]
    newCurve = rs.JoinCurves(crvs,True)[0]
    
    reference = SubObjectSelect()
    surface = reference[0]
    point = reference[1]
    if surface is None: return False
    point = reference[1]
    if point is None: return False
    distance = 4
    offset = rs.OffsetCurveOnSurface( newCurve, surface, distance )
    if not offset: rs.OffsetCurveOnSurface( newCurve, surface, -1*distance )
    return offset
def SubObjectSelect():
    obj_ref = rs.GetObject(message="Bla", filter=8, preselect=False, subobjects=True)
    if obj_ref:
        return  [obj_ref.Surface(),obj_ref.SelectionPoint()]
        print "Surface:", obj_ref.Surface()
        print "Selection Point:", obj_ref.SelectionPoint()
TestOffset()