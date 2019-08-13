"""
  plot some sinusoid with matplotlib,
  and statically serve it through flask, without any disk I/O

  python >3 version (io package instead of StringIO)

	usage :   python flaskPlot.py
            wget http://127.0.0.1:5000/sin/
            wget http://127.0.0.1:5000/sin/[0;12]
"""

from io import BytesIO
from flask import Flask, send_file
import matplotlib.pyplot as plt

import numpy as np

app = Flask(__name__)

@app.route('/sin/')
@app.route('/sin/[<int:min>;<int:max>]')
def plot_sinus(min = 0, max = 5):

	# generate sinus data
	x = np.arange(min, max, 0.1);
	y = np.sin(x)

	# plot data with pyplot
	plt.figure()
	plt.plot(x, y)
	plt.title("sinus")

	# save this pyplot into a BytesIO string
	byte_io = BytesIO()
	plt.savefig(byte_io, format='png')
	byte_io.seek(0)

	# return the png using send_file Flask function
	return send_file(byte_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
