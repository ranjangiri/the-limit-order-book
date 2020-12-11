from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
from flask import Flask,request,render_template
import json
app=Flask(__name__)




orderbookask={"ask5":[11.38,400],
"ask4":[11.39,1600] ,
"ask3":[11.40,1205],
"ask2":[11.41, 1400],
    "ask1":[11.42 ,900]
		 }
orderbookbid={"bid1":[2700 ,11.36],
  "bid2":[1100,11.35],
  "bid3":[1100,11.34 ],
  "bid4":[1600 ,11.33],
    "bid5":[700 ,11.32 ]
              }

data4={
    "ask5":[11.38,400],
"ask4":[11.39,1600],
"ask3":[11.40,1205] ,
"ask2":[11.41, 1400] ,
    "ask1":[11.42 ,900]
		  }
data5={"bid1":[2700 ,11.36],
  "bid2":[1100,11.35],
  "bid3":[1100,11.34 ],
  "bid4":[1600 ,11.33],
    "bid5":[700 ,11.32 ] }


@app.route("/",methods=['POST','GET'])
def run():
    page2=None
    page = request.args.get("link1")
    if page:
        page2="on"

    if request.method == 'POST':
        datapan = request.form
        stock=None
        stock_price=None
        try:
            if datapan["stock"] and datapan["stock_price"]:
                stock=datapan["stock"]
                stock_price=datapan["stock_price"]
        except:
            return "please select appropriate  to buy"

        try:
            if datapan["sell"]=="on":
                Entering_a_market("sell", stock, stock_price)
        except:
            if datapan["buy"]=="on":
                Entering_a_market("buy", stock, stock_price)
    return render_template("index.html",data=orderbookask ,data2=orderbookbid,data3=page2,data4=data4,data5=data5,time=current_time)

def Entering_a_market(sell,stock,stock_price):
    No_of_shares=int(stock)
    d=sell
    e=stock_price
    if d=="sell":
        for i,j in data4.items():
            if float(e)==float(j[0]):
                if int(No_of_shares)<=int(j[1]):
                    data4[i]=[j[0],int(j[1])-int(No_of_shares)]
                    print(data4)
                    print(orderbookask)
                    return data4
    elif d=="buy":
        for i,j in data5.items():
            print(float(e),float(j[1]))
            if float(e)==float(j[1]):
                print("hinuvhd")
                if int(No_of_shares)<=int(j[0]):
                    print("sdfjfsj")
                    data5[i]=[int(j[0])+int(No_of_shares),j[1]]

                    print(orderbookbid)
                    return data5
if __name__=="__main__":
    app.run(debug=True)




