from flask import Flask, request, render_template
# Flask constructor
import alignment
app = Flask(__name__)

# `flask --debug run` for automatically update while running

# A decorator used to tell the application
# which URL is associated function


@app.route('/align', methods=["GET", "POST"])
def align():
   keys = ['A', 'C', 'T', 'G', '-']
   delta = {}
   for i in range(len(keys)):
      delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
   if request.method == "POST":
      # getting input with name = fname in HTML form
      s1 = request.form.get("s1")
      # getting input with name = lname in HTML form
      s2 = request.form.get("s2")
      type = request.form['options']
      if (type and s1 and s2):
         # input will be len(s1)<len(s2), so space complexity will be O(len(s1))
         if (len(s2) < len(s1)):
            s1, s2 = s2, s1
         align1, align2, alignCorrds = alignment.align(s1, s2, delta, type)
         return render_template("pages/align.html", type = type, align1 = align1, align2 = align2, s1 = s1, s2 = s2, alignCorrds = alignCorrds)
      else:
         return render_template("pages/align.html")
   return render_template("pages/align.html")


@app.route('/intro')
def intro():
    return render_template('pages/intro.html')


@app.route('/')
def main():
    return render_template('pages/main.html')


if __name__ == '__main__':
    app.run()
