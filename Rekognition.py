import boto3
from botocore.exceptions import ClientError

def obtener_bytes_imagen(ruta_imagen):
    with open(ruta_imagen, "rb") as imagen:
        return imagen.read()

def comparar_rostros(ruta_imagen1,ruta_imagen2):
    bytes_1 = obtener_bytes_imagen(ruta_imagen1)
    bytes_2 = obtener_bytes_imagen(ruta_imagen2)

    cliente = boto3.client('rekognition')
    try:
        respuesta = cliente.compare_faces(SourceImage = {'Bytes' : bytes_1}, 
                                          TargetImage = {'Bytes': bytes_2},
                                          SimilarityThreshold = 60,
                                          QualityFilter = 'NONE')
        
    except ClientError as error:
        print("Error al llamar la API:",error)

    if respuesta and respuesta.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        # UnmatchedFaces
        for i in respuesta['UnmatchedFaces']:
            print("Unmatched Faces")
            print('\n')

        # FaceMatches
        for i in respuesta['FaceMatches']:

            # SIMILARITY
            print('Similarity: ', i['Similarity'])
            

if __name__ == "__main__":
    comparar_rostros('/home/kali/Pictures/Messi1.jpg','/home/kali/Pictures/N1.jpg')