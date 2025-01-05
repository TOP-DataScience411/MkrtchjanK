import datetime
import decimal
import numbers

class PowerMeter:
    # Класс, описывающий двухтарифный счетчик потребленной электрической мощности
    def __init__(self, 
                 tariff1: numbers.Number = 6.5, 
                 tariff2: numbers.Number = 5.0, 
                 tariff2_starts: datetime.time = datetime.time(22, 0), 
                 tariff2_ends: datetime.time = datetime.time(6, 0)):
        self.tariff1 = decimal.Decimal(tariff1)
        self.tariff2 = decimal.Decimal(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = decimal.Decimal(0)
        self.charges: Dict[datetime.date, decimal.Decimal] = {}
    def __repr__(self):
        # Машиночитаемое строковое представление.
        return f"<PowerMeter: {self.power} кВт/ч>"

    def __str__(self):
        # Человекочитаемое строковое представление.
        total_charge = sum(self.charges.values())
        month = datetime.datetime.now().strftime("%b")
        return f"({month}) {total_charge:.2f}"

    def meter(self, power: numbers.Number) -> decimal.Decimal:
        # Вычисляет стоимость потреблённой мощности согласно тарифному плану.
        current_time = datetime.datetime.now().time()
        if self.tariff2_starts <= current_time or current_time <= self.tariff2_ends:
            cost = self.tariff2 * decimal.Decimal(power)
        else:
            cost = self.tariff1 * decimal.Decimal(power)

        self.power += decimal.Decimal(power)
        today = datetime.datetime.now().date()
        if today not in self.charges:
            self.charges[today] = decimal.Decimal(0)
        self.charges[today] += cost
        return cost.quantize(decimal.Decimal('0.01'))
       

#>>> pm1 = PowerMeter()
#>>> 
#>>> pm1.meter(2)
#Decimal('13.00')
#>>> pm1.meter(1.2)
#Decimal('7.80')
#>>> 
#>>> pm1
#<PowerMeter: 3.2 кВт/ч>
#(Jan) 20.80

