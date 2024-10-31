{"cells":[{"cell_type":"code","execution_count":1,"metadata":{"executionInfo":{"elapsed":589,"status":"ok","timestamp":1730360288623,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"},"user_tz":0},"id":"Lodtps2nu_-s"},"outputs":[],"source":["!rm -f ngrok\n","!rm -f /usr/local/bin/ngrok\n","!rm -rf /root/.ngrok2"]},{"cell_type":"code","execution_count":2,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"collapsed":true,"executionInfo":{"elapsed":1535,"status":"ok","timestamp":1730360290155,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"},"user_tz":0},"id":"NJtKus3gxkGJ","outputId":"1ccebaa1-ad54-4db9-8b72-149eb85b277b"},"outputs":[{"output_type":"stream","name":"stdout","text":["--2024-10-31 07:38:08--  https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip\n","Resolving bin.equinox.io (bin.equinox.io)... 13.248.244.96, 99.83.220.108, 75.2.60.68, ...\n","Connecting to bin.equinox.io (bin.equinox.io)|13.248.244.96|:443... connected.\n","HTTP request sent, awaiting response... 200 OK\n","Length: 9153340 (8.7M) [application/octet-stream]\n","Saving to: ‘ngrok.zip’\n","\n","ngrok.zip           100%[===================>]   8.73M  18.6MB/s    in 0.5s    \n","\n","2024-10-31 07:38:08 (18.6 MB/s) - ‘ngrok.zip’ saved [9153340/9153340]\n","\n","Archive:  ngrok.zip\n","  inflating: ngrok                   \n"]}],"source":["# Download and unzip the latest version of ngrok\n","!wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip -O ngrok.zip\n","!unzip -o ngrok.zip"]},{"cell_type":"code","execution_count":3,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"collapsed":true,"executionInfo":{"elapsed":12327,"status":"ok","timestamp":1730360302478,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"},"user_tz":0},"id":"HhB42SpTCP7h","outputId":"ebd5de4d-23b9-4062-969f-350cf913c21b"},"outputs":[{"output_type":"stream","name":"stdout","text":["Requirement already satisfied: flask_ngrok in /usr/local/lib/python3.10/dist-packages (0.0.25)\n","Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.10/dist-packages (from flask_ngrok) (2.2.5)\n","Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from flask_ngrok) (2.32.3)\n","Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (3.0.6)\n","Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (3.1.4)\n","Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (2.2.0)\n","Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (8.1.7)\n","Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (3.4.0)\n","Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (3.10)\n","Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (2.2.3)\n","Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (2024.8.30)\n","Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from Jinja2>=3.0->Flask>=0.8->flask_ngrok) (3.0.2)\n","Requirement already satisfied: pyngrok in /usr/local/lib/python3.10/dist-packages (7.2.0)\n","Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.2)\n","Requirement already satisfied: Flask-WTF in /usr/local/lib/python3.10/dist-packages (1.2.2)\n","Requirement already satisfied: flask in /usr/local/lib/python3.10/dist-packages (from Flask-WTF) (2.2.5)\n","Requirement already satisfied: itsdangerous in /usr/local/lib/python3.10/dist-packages (from Flask-WTF) (2.2.0)\n","Requirement already satisfied: wtforms in /usr/local/lib/python3.10/dist-packages (from Flask-WTF) (3.2.1)\n","Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.10/dist-packages (from flask->Flask-WTF) (3.0.6)\n","Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from flask->Flask-WTF) (3.1.4)\n","Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from flask->Flask-WTF) (8.1.7)\n","Requirement already satisfied: markupsafe in /usr/local/lib/python3.10/dist-packages (from wtforms->Flask-WTF) (3.0.2)\n"]}],"source":["!pip install flask_ngrok\n","!pip install pyngrok\n","!pip install Flask-WTF"]},{"cell_type":"code","execution_count":4,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":11,"status":"ok","timestamp":1730360302478,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"},"user_tz":0},"id":"Hxc08a9Hx04E","outputId":"d575fc41-e93a-4eb7-9e41-6c5e15ad6e25"},"outputs":[{"output_type":"stream","name":"stdout","text":["ngrok version 3.18.1\n"]}],"source":["!./ngrok version"]},{"cell_type":"code","execution_count":5,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"collapsed":true,"executionInfo":{"elapsed":251,"status":"ok","timestamp":1730360302722,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"},"user_tz":0},"id":"ornsLVLI0kP_","outputId":"8b424d6b-f7ea-4bd2-d1ff-3305a18ac40e"},"outputs":[{"output_type":"stream","name":"stdout","text":["Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n"]}],"source":["# Authenticate using your ngrok token\n","!./ngrok authtoken 2o4pfmzyiwmBZcY4vhwQiYsOiJS_FsuQB2nueaQ863GcU2ya"]},{"cell_type":"code","execution_count":17,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"N3AmKWEFNRBb","executionInfo":{"status":"ok","timestamp":1730361400463,"user_tz":0,"elapsed":17745,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"}},"outputId":"7134a547-a781-4c2c-a891-b0c1c69b31f6"},"outputs":[{"output_type":"stream","name":"stdout","text":["Ngrok tunnel URL: NgrokTunnel: \"https://d275-34-73-115-48.ngrok-free.app\" -> \"http://localhost:5000\"\n"," * Serving Flask app '__main__'\n"," * Debug mode: off\n"]},{"output_type":"stream","name":"stderr","text":["INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n"," * Running on http://127.0.0.1:5000\n","INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n"]}],"source":["from flask import Flask, request, redirect, url_for, render_template, jsonify\n","from pyngrok import ngrok\n","import atexit\n","import os\n","\n","app = Flask(__name__, template_folder='/content/drive/MyDrive/ColabNotebooks/Receipt_itemizer/templates')\n","ngrok.set_auth_token(os.getenv(\"NGROK_AUTH_TOKEN\", \"2o4pfmzyiwmBZcY4vhwQiYsOiJS_FsuQB2nueaQ863GcU2ya\"))\n","public_url = ngrok.connect(5000)\n","print(\"Ngrok tunnel URL:\", public_url)\n","\n","class RestaurantReceipt:\n","    def __init__(self):\n","        self.items = []\n","        self.eaters = set()\n","        self.receipt_name = \"\"\n","\n","    def set_receipt_name(self, name):\n","        self.receipt_name = name\n","\n","    def enter_eaters(self, eaters):\n","        self.eaters = {eater.strip().title() for eater in eaters.split(\",\")}\n","\n","    def add_item(self, item_name, item_price, eaters_input):\n","        if eaters_input.strip().upper() == \"ALL\":\n","            eaters_list = list(self.eaters)\n","        else:\n","            eaters_list = [eater.strip().title() for eater in eaters_input.split(\",\") if eater.strip().title() in self.eaters]\n","\n","        if not eaters_list:\n","            return \"No valid eaters provided. Maybe you should invite them next time. No item added.\"\n","\n","        self.items.append({\n","            'name': item_name,\n","            'price': item_price,\n","            'eaters': eaters_list\n","        })\n","\n","    def calculate_total_sum(self):\n","        return sum(item['price'] for item in self.items)\n","\n","    def calculate_per_person_share(self):\n","        per_person = {eater: 0 for eater in self.eaters}\n","        for item in self.items:\n","            split_cost = item['price'] / len(item['eaters'])\n","            for eater in item['eaters']:\n","                per_person[eater] += split_cost\n","        return per_person\n","\n","    def display_receipt(self):\n","        return {\n","            \"receipt_name\": self.receipt_name,\n","            \"items\": self.items,\n","            \"total_sum\": self.calculate_total_sum(),\n","            \"per_person_share\": self.calculate_per_person_share()\n","        }\n","\n","receipt_manager = RestaurantReceipt()\n","\n","# Redirect root route to receipt manager page\n","@app.route('/')\n","def home():\n","    return redirect(url_for('receipt_manager_page'))\n","\n","@app.route('/receipt_manager')\n","def receipt_manager_page():\n","    receipt_data = receipt_manager.display_receipt()\n","    return render_template('receipt_manager.html', receipt_data=receipt_data)\n","\n","@app.route('/initialize_receipt', methods=['POST'])\n","def initialize_receipt():\n","    name = request.form['name']\n","    eaters = request.form['eaters']\n","    receipt_manager.set_receipt_name(name)\n","    receipt_manager.enter_eaters(eaters)\n","    return redirect(url_for('receipt_manager_page'))\n","\n","@app.route('/add_item', methods=['POST'])\n","def add_item():\n","    item_name = request.form['item_name']\n","    try:\n","        item_price = float(request.form['item_price'])\n","    except ValueError:\n","        return jsonify({\"error\": \"Invalid price format.\"}), 400\n","    eaters_input = request.form['eaters_input']\n","    result = receipt_manager.add_item(item_name, item_price, eaters_input)\n","    if result:\n","        return jsonify({\"error\": result}), 400\n","    return redirect(url_for('receipt_manager_page'))\n","\n","atexit.register(ngrok.disconnect, public_url)\n","\n","if __name__ == \"__main__\":\n","    app.run(port=5000)\n"]},{"cell_type":"code","source":["%%writefile /content/drive/MyDrive/ColabNotebooks/Receipt_itemizer/templates/receipt_manager.html\n","<!DOCTYPE html>\n","<html>\n","<head>\n","    <title>Receipt Manager</title>\n","    <style>\n","        body { font-family: Arial, sans-serif; background-color: #f0f8ff; padding: 50px; }\n","        .container { display: flex; flex-direction: column; gap: 20px; }\n","        .top-container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }\n","        .form-column, .receipt-column { width: 45%; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }\n","        .bottom-container { display: flex; gap: 20px; }\n","        h2, h3, h4 { color: #4682b4; }\n","        ul { list-style-type: none; padding: 0; }\n","        li { margin: 10px 0; }\n","        form { text-align: left; }\n","        label, input { display: block; width: 100%; margin-bottom: 10px; }\n","        input[type=\"submit\"] { background-color: #4682b4; color: white; border: none; padding: 10px; cursor: pointer; }\n","        .back-button { text-align: left; margin-bottom: 20px; }\n","        .back-button a { background-color: #4682b4; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px; }\n","    </style>\n","</head>\n","<body>\n","    <div class=\"container\">\n","        <div class=\"top-container\">\n","            <div class=\"back-button\">\n","                <a href=\"{{ url_for('home') }}\">Back to Home</a>\n","            </div>\n","            <h2>Initialize Receipt</h2>\n","            <form action=\"{{ url_for('initialize_receipt') }}\" method=\"post\">\n","                <label>Enter Receipt Name:</label>\n","                <input type=\"text\" name=\"name\" required>\n","                <label>Enter Eaters (comma-separated):</label>\n","                <input type=\"text\" name=\"eaters\" required>\n","                <input type=\"submit\" value=\"Initialize Receipt\">\n","            </form>\n","        </div>\n","\n","        <div class=\"bottom-container\">\n","            <div class=\"form-column\">\n","                <h2>Add Item</h2>\n","                <form action=\"{{ url_for('add_item') }}\" method=\"post\">\n","                    <label>Item Name:</label>\n","                    <input type=\"text\" name=\"item_name\" required>\n","                    <label>Item Price (£):</label>\n","                    <input type=\"text\" name=\"item_price\" required>\n","                    <label>Eaters (comma-separated, or 'ALL'):</label>\n","                    <input type=\"text\" name=\"eaters_input\" required>\n","                    <input type=\"submit\" value=\"Add Item\">\n","                </form>\n","            </div>\n","\n","            <div class=\"receipt-column\">\n","                <h3>Current Receipt: {{ receipt_data['receipt_name'] }}</h3>\n","                <ul>\n","                    {% for item in receipt_data['items'] %}\n","                        <li>{{ item['name'] }}: £{{ \"%.2f\"|format(item['price']) }} (shared by {{ \", \".join(item['eaters']) }})</li>\n","                    {% endfor %}\n","                </ul>\n","                <p>Total: £{{ \"%.2f\"|format(receipt_data['total_sum']) }}</p>\n","                <h4>Cost Breakdown Per Person</h4>\n","                <ul>\n","                    {% for person, amount in receipt_data['per_person_share'].items() %}\n","                        <li>{{ person }}: £{{ \"%.2f\"|format(amount) }}</li>\n","                    {% endfor %}\n","                </ul>\n","            </div>\n","        </div>\n","    </div>\n","</body>\n","</html>\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"UoUjRVZ-jxQr","executionInfo":{"status":"ok","timestamp":1730361115426,"user_tz":0,"elapsed":266,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"}},"outputId":"d474de12-278a-411a-adc6-e5a38885ac04"},"execution_count":13,"outputs":[{"output_type":"stream","name":"stdout","text":["Writing /content/drive/MyDrive/ColabNotebooks/Receipt_itemizer/templates/receipt_manager.html\n"]}]},{"cell_type":"code","source":["%%writefile /content/drive/MyDrive/ColabNotebooks/Receipt_itemizer/requirements.txt\n","Flask\n","pyngrok\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"ytDTYoYGzcht","executionInfo":{"status":"ok","timestamp":1730365217262,"user_tz":0,"elapsed":313,"user":{"displayName":"Jamie Hill","userId":"10831983047187267053"}},"outputId":"0eda2de3-e06e-48b7-8b29-0d13743ce506"},"execution_count":18,"outputs":[{"output_type":"stream","name":"stdout","text":["Writing /content/drive/MyDrive/ColabNotebooks/Receipt_itemizer/requirements.txt\n"]}]}],"metadata":{"colab":{"provenance":[],"mount_file_id":"1viNmg-Df1jQbSoUT15OI5K_fFTMbQLOh","authorship_tag":"ABX9TyObOCX4obyLQ4v+HQBbDREm"},"kernelspec":{"display_name":"Python 3","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":0}