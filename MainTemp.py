################################################################################
# SampleEtoViewports.py
# Copyright (c) 2017 Robert McNeel & Associates.
# See License.md in the root of this repository for details.
################################################################################
import Rhino
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino as rh
import csv

################################################################################
# Viewports dialog class
################################################################################
class ViewportsDialog(forms.Dialog[bool]):
    
    # Initializer
    def __init__(self):
        # Initialize dialog box
        self.Title = 'Dynamis'
        self.Padding = drawing.Padding(5)
        self.Resizable = False
        
        self.m_image_view = forms.ImageView()
        self.m_image_view.Size = drawing.Size(400, 225)
        self.m_image_view.Image =drawing.Bitmap("D:\AnimazioneBot\Vect.PNG")
        # Create layout

        self.m_button = forms.Button(Text = 'Esporta')
        self.m_button.Click += self.LanciaBotton

        self.m_textbox = forms.TextBox()
        self.m_label = forms.Label(Text = 'Indica il nome del progetto:')
        self.m_textbox.Text = "untitled"


        self.m_foronumero = forms.TextBox()
        self.m_forolabel = forms.Label(Text = 'Indica la dimensione del foro')
        self.m_foronumero.Text = "10"
        layout = forms.DynamicLayout()
        layout.Padding = drawing.Padding(5)
        layout.Spacing = drawing.Size(5, 5)
        layout.BeginVertical()
        layout.AddSeparateRow(None,self.m_image_view,None)
        layout.EndVertical()
        layout.AddRow(None)
        layout.BeginVertical()
        layout.AddRow(None,self.m_label,None,self.m_textbox,None)
        layout.EndVertical()
        layout.AddRow(None)
        layout.BeginVertical()
        layout.AddRow(None,self.m_forolabel,None,self.m_foronumero,None)
        layout.EndVertical()
        layout.AddRow(None)
        layout.BeginVertical()
        layout.AddRow(None,self.m_button,None,self.CloseButton(),None)
        layout.EndVertical()
        # Set the dialog content
        self.Content = layout
        

    def GetText(self):
        return self.m_textbox.Text


    def OnCloseButtonClick(self, sender, e):
        self.Close(True)
       
       



    def LanciaBotton(self, sender, e):
        self.Close(True)
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
                    
            for CurveId in CurveIdList: 

                if rs.IsCircle(CurveId):

                    Pt = rs.CircleCenterPoint(CurveId)
                    Normal = rs.CurveNormal(CurveId)
                    LenghtNormal = rs.VectorLength(Normal)
                    LenghNormal = self.m_foronumero.Text
                    LenghNormal = int(LenghNormal)
                    Normal = (LenghNormal*Normal[0],LenghNormal*Normal[1],LenghNormal*Normal[2])
                    PtStill = rs.AddPoint(Pt)

                    Ptmoved = rs.MoveObject(Pt,Normal)
                    Ptmoved = rs.coerce3dpoint(Ptmoved)
                    PtStill = rs.coerce3dpoint(PtStill)

                    PointPlane.append([PtStill[0],PtStill[1],PtStill[2],Normal[0],Normal[1],Normal[2]])
                    #PointPlane.append([Ptmoved[0],Ptmoved[1],Ptmoved[2],Normal[0],Normal[1],Normal[2]])
            return (PointPlane,Brep)
        
        
        def CSVwrite(list,folder):
            #Get the filename to create
            filename = folder+"\\"+self.m_textbox.Text+"punti"+".csv"
            print filename
            with open(filename, "wb") as csvfile:
                csvwriter = csv.writer(csvfile,  delimiter=',')
                for item in list:
                    csvwriter.writerow(item)
                print "Points written sucessfully to file"
        def exportBrep(Brep,folder):
            
            Brep = Brep[0]
            rs.SelectObject(Brep)
            file = folder + "\\"+ self.m_textbox.Text+ "solido"+ ".step"
            extension = ".step"
            export = rs.Command("_-Export " + file+ " _Enter")
        def Export (Object):
            folder = rs.BrowseForFolder("Questo PC","seleziona dove vuoi salvare i tuoi file")
            CSVwrite(Object[0],folder)
            exportBrep(Object[1],folder)
                
        PtNormBrep = FromEdgetoPlane()
        Export(PtNormBrep)
        rs.Command("_SelNone")
        rs.Command("_SelPt")
        rs.Command("_SelCrv")
        rs.Command("_Delete")
        for viewport in viste:
            rs.ViewDisplayMode(viewport,"Shaded")
        self.Close(True)

################################################### fine definizione point extractor
            
        
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

