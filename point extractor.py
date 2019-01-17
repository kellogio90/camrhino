
import rhinoscriptsyntax as rs
import Rhino as rh
import csv
def FromEdgetoPlane ():
    PointPlane = []
    CurveIdList = []
    Brep = []
    edges = rs.GetEdgeCurves()
    if edges:
        for edgeinfo in edges:
            Brep.append (edgeinfo[1])
            CurveIdList.append (edgeinfo[0])
#    print CurveIdList
    for CurveId in CurveIdList: 
        
        if rs.IsCircle(CurveId):
#            print "Sono un cerchio"
            Pt = rs.CircleCenterPoint(CurveId)
            Normal = rs.CurveNormal(CurveId)
            LenghtNormal = rs.VectorLength(Normal)
            LenghNormal = rs.GetString("give me the lengh of the hole","100")
            LenghNormal = int(LenghNormal)
            Normal = (LenghNormal*Normal[0],LenghNormal*Normal[1],LenghNormal*Normal[2])
            print Normal
            PtStill = rs.AddPoint(Pt)
            Ptmoved = rs.MoveObject(Pt,Normal)
            Ptmoved = rs.coerce3dpoint(Ptmoved)
            PtStill = rs.coerce3dpoint(PtStill)
#            print Ptmoved
#            print PtStill

            PointPlane.append([PtStill[0],PtStill[1],PtStill[2],Normal[0],Normal[1],Normal[2]])
            #PointPlane.append([Ptmoved[0],Ptmoved[1],Ptmoved[2],Normal[0],Normal[1],Normal[2]])
    return (PointPlane,Brep)
    
    



def CSVwrite(list,folder):
    #Get the filename to create
    filename = folder+".csv"
    print filename
    with open(filename, "wb") as csvfile:
        csvwriter = csv.writer(csvfile,  delimiter=',')
        for item in list:
            csvwriter.writerow(item)
        print "Points written sucessfully to file"
def exportBrep(Brep,folder):
    Brep = Brep[0]
    rs.SelectObject(Brep)
    rs.Command("_-Export "+str(folder)+"par"+".step"+" _Enter")
def Export (Object):
        folder = rs.BrowseForFolder("Questo PC","seleziona dove vuoi salvare i tuoi file")
        folder = folder+ "\Parafango"
        CSVwrite(Object[0],folder)
        exportBrep(Object[1],folder)

if __name__=="__main__":
    PtNormBrep = FromEdgetoPlane()
    Export(PtNormBrep)
