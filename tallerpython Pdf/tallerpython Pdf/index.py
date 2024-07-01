import PyPDF2
import pandas as pd

def ejercio(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        tabletestarctura = False
        tabla_con_los_datos = []
        
        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text()
            lines = page_text.split('\n')
            
            for line in lines:
                if "37910" in line:
                    tabletestarctura = True
                
                if tabletestarctura:
                    columns = line.split()
                    if len(columns) >= 11:  
                       
                        fecha = f"{columns[1]}, {columns[2]} {columns[3]} {columns[4]} {columns[5]} {columns[6]}"
                        codigo = columns[0]
                        ciudad_departamento = columns[7]
                        tipo_bien = columns[8]
                        avaluo_remate = columns[9]
                        oferta_minima = columns[10]
                        referencia = columns[11] if len(columns) > 9 else None
                        tabla_con_los_datos.append([codigo, fecha, ciudad_departamento, tipo_bien, avaluo_remate, oferta_minima, referencia])
        
        df = pd.DataFrame(tabla_con_los_datos, columns=["CÓDIGO", "Fecha del remate", "Ciudad" ,"Departamento", "Tipo de bien", "Avaluo remate", "Oferta Mínima"])
        return df

pdf_ruta = "Remates.pdf"
tabla = ejercio(pdf_ruta)
tabla.to_excel("tabla_remates.xlsx", index=False)

print("Tabl extraida y convertica e Excel")
