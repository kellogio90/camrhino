import rhinoscriptsyntax as rs
import csv


class TestViewportsDialog():
    #codice point extractor
    viste = rs.ViewNames()
    for viewport in viste:
        rs.ViewDisplayMode(viewport,"Ghosted")
    def FromEdgetoPlane ():
        PointPlane = []
        CurveIdList = []
        Brep = []
        edges = rs.GetEdgeCurves()
        if edges:
            for edgeinfo in edges:
                Brep.append (edgeinfo[1])
                CurveIdList.append (edgeinfo[0])
                print CurveIdList
        for CurveId in CurveIdList: 
            
            if rs.IsCircle(CurveId):
    #            print "Sono un cerchio"
                Pt = rs.CircleCenterPoint(CurveId)
                Normal = rs.CurveNormal(CurveId)
                LenghtNormal = rs.VectorLength(Normal)
                LenghNormal = self.m_foronumero.Text
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
    PtNormBrep = FromEdgetoPlane()
    
    
    
    def CSVwrite(list,folder):
        #Get the filename to create
        filename = folder+"punti"+".csv"
        print filename
        with open(filename, "wb") as csvfile:
            csvwriter = csv.writer(csvfile,  delimiter=',')
            for item in list:
                csvwriter.writerow(item)
            print "Points written sucessfully to file"
    def exportBrep(Brep,folder):
        Brep = Brep[0]
        rs.SelectObject(Brep)
        rs.Command("_-Export "+str(folder)+"solido"+".step"+" _Enter")
    def Export (Object):
            folder = rs.BrowseForFolder("Questo PC","seleziona dove vuoi salvare i tuoi file")
            folder = folder+"\\" + "parafango"
            print str(folder)
            CSVwrite(Object[0],folder)
            exportBrep(Object[1],folder)
    
    Export(PtNormBrep)
    rs.Command("_SelNone")
    rs.Command("_SelPt")
    rs.Command("_SelCrv")
    rs.Command("_Delete")
    for viewport in viste:
        rs.ViewDisplayMode(viewport,"Shaded")
    
    
    ################################################### fine definizione point extractor
        
        
    
    def Colorreturner(self):
        return self.m_slider.Value
    def CloseButton(self):
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'Close')
        self.DefaultButton.Click += self.OnCloseButtonClick
        return self.DefaultButton
    
    ################################################################################
    # Function to test the viewport dialog
    ################################################################################
    def TestViewportsDialog():
        dlg = ViewportsDialog()
        rc = dlg.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)

 
################################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
################################################################################
if __name__ == "__main__":
    TestViewportsDialog()
