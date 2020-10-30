class Car():
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):

    self.g_type = gear_type
    print(self.g_type + " gear changed")    # gear related functionality here


maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
maruthi_suzuki.start()
maruthi_suzuki.stop()
maruthi_suzuki.accelarate()
maruthi_suzuki.change_gear('2nd')
maruthi_suzuki.change_gear('3rd')




audi = Car("A6", "red", "audi", 80)