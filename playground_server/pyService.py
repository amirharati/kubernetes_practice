"""
    Simple backend server to execute python code.
"""

from flask import Flask, request
from flask import jsonify
from subprocess import Popen, PIPE
import uuid
app = Flask(__name__, static_url_path='')
@app.route("/py/eval", methods=['GET', 'POST'])
def handle():
    if request.method == 'POST':#
        content = request.json                                                                                                               
        code = content["code"]
        fname = "./tmp/" + str(uuid.uuid4()) + ".py"
        with open(fname, "w") as fo:
            fo.write(code + "\n")
        cmd = "python3 " + fname
        p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
        stdo, stde = p.communicate()
        return jsonify(
                     stdout=stdo.decode("utf-8"), stderr=stde.decode("utf-8")
                 )
    return("hi")
                                                                                                              
if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)
