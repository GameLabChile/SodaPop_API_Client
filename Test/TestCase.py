from unittest import TestCase
import urllib
import urllib2
import httplib2
import rsa
import base64
import json
import time
import psycopg2

# Create your tests here.


class Test_API(TestCase):


    def escenarios(self):
        conn = psycopg2.connect(database='sodapop',user='gm',password='1qaz2wsx3edc', host='sp-db.c1r9lrlagsae.sa-east-1.rds.amazonaws.com')

        cur = conn.cursor()
        cur.execute("select id,name from stage")
        row = cur.fetchall()
        return row


    def test_iniciar_partida(self):
        """
        ejecuta login y retorna una cookie de sesion
        """

        try:

            '''
            teacher:gamelab@gamelab.cl
            player:fabian
            esc:13
            time:1456950682
            playerid:1
            classid:1
            sign:ha58QowTPowDTLH2GszerwOCGkvoaiRQAcaBMJ17FO8MziF8JpY0jHdJvTjSkWf04HMnKDEg7s4HGjfNXoRWs854jd8aqAe3wIY2JB2PPPx2rg9JO0WHtrDg9fE14_oXL1950xXeoltXfEcH9PhzHYZjzuo9PwfdSoc70BxwWkc=
            '''

            player = raw_input("Ingrese nombre del jugador")

            for n in self.escenarios():
                print n


            esc = int(raw_input("Numero de escenarios"))
            playerid= 1
            classid= 1
            timereq = int(time.time())
            url = "https://sp-dev.gamelab.cl/api/newalone/"
            teacher = "gamelab@gamelab.cl"
            private_key = rsa.PrivateKey(135029684411836463323964252311790626420400824319263974720208824508437555654491291055113056194717508477434017708517506511910833292985521483489975993602890988197575597070937122972491618562349497007864811663127671552248579928236273284258790781773463479851013106516802197673233261103509191605822028096277111075231, 65537, 50264494574227724174915420287752630150176213590685626856191380177729261451500214177953493735238542148946096037612235666334691685851881869954704260400396125434896645221343051223960866327111196984114078198171257253271590528258718113313362450273038415511547479748000208882114602008719312717006430786322599148385, 50257229368562109885338782933612258651709692866444619540597165173015610870283328852282373562840583893831293648363897477049170184711382683997893270326484073310654099, 2686771358237724223760351067489467424579917667965738372521998271592464919902841310973472093092338759084824283806654525898847227449503529256217669) #key given

            cantidad = int(raw_input("Cantidad de jugadores"))

            i=1
            while i < cantidad+1:
                data = {
                    'teacher':teacher,
                    'player':player+str(i),
                    'time':timereq,
                    'esc':esc,
                    'playerid': int(playerid),
                    'classid':int(classid)
                }
                firma = rsa.sign( json.dumps(data, sort_keys=True) , private_key, 'SHA-1' )
                firma64 = base64.urlsafe_b64encode(firma)

                data_post = {
                    'teacher':teacher,
                    'player':player+str(i),
                    'time':timereq,
                    'esc':esc,
                    'playerid': int(playerid),
                    'classid':int(classid),
                    'sign': firma64
                }

                headers = {'Content-type': 'application/x-www-form-urlencoded'}

                encoded_data = urllib.urlencode(data_post)

                http = httplib2.Http(disable_ssl_certificate_validation=True)
                response, content = http.request(
                            url,
                            "POST",
                            body=encoded_data,
                            headers=headers)
                print player+str(i)
                print response
                i+=1
        except:
            pass

