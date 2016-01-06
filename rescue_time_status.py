import rumps
import urllib2
import json
import webbrowser

class RescueTimeStatus(rumps.App):
  def __init__(self):
    super(RescueTimeStatus, self).__init__("RescueTime Productivity")
    self.menu = ["Details", None]
    self.update_stats()

  @rumps.timer(54000) # 15 minutes
  def peridioc_update(self, sender):
    self.update_stats()

  def update_stats(self):
    data = urllib2.urlopen("https://www.rescuetime.com/anapi/data/?rs=day&format=json&key=B63SVy_FSp7iDJCTfniTjitbQrUcUwZhzaShpERO&rk=efficiency&pv=interval").read()
    data = json.loads(data)

    prod_pulse = str(int(round(data['rows'][0][4])))
    time_logged = data['rows'][0][1]

    self.title = prod_pulse

  @rumps.clicked("Details")
  def go_to_dashboard(self):
    webbrowser.open_new("https://www.rescuetime.com/dashboard")

if __name__ == "__main__":
  RescueTimeStatus().run()