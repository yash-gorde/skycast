import tkinter as tk
from tkinter import ttk
import requests
import tkintermapview

class SkycastApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Visualize Through Skycast Application")
        self.window.config(bg="pink")
        self.window.geometry(f"{550}x{550}+170+120")
        
        self.city_coordinates = {
            "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Tirupati", "Kakinada"],
            "Arunachal Pradesh": ["Itanagar", "Tawang", "Ziro", "Naharlagun", "Pasighat"],
            "Assam": ["Guwahati", "Dibrugarh", "Jorhat", "Nagaon", "Silchar"],
            "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Nalanda"],
            "Chhattisgarh": ["Raipur", "Bhilai", "Durg", "Bilaspur", "Korba"],
            "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda"],
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar"],
            "Haryana": ["Chandigarh", "Faridabad", "Gurgaon", "Ambala", "Hisar"],
            "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Kullu", "Solan"],
            "Jammu and Kashmir": ["Srinagar", "Jammu", "Poonch", "Udhampur", "Anantnag"],
            "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh"],
            "Karnataka": ["Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum"],
            "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Kollam", "Malappuram"],
            "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Sangamner"],
            "Manipur": ["Imphal", "Thoubal", "Churachandpur", "Bishnupur", "Senapati"],
            "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongstoin", "Williamnagar"],
            "Mizoram": ["Aizawl", "Lunglei", "Kolasib", "Champhai", "Serchhip"],
            "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Wokha", "Zunheboto"],
            "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur"],
            "Punjab": ["Amritsar", "Ludhiana", "Jalandhar", "Patiala", "Bathinda"],
            "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur", "Kota", "Ajmer"],
            "Sikkim": ["Gangtok", "Namchi", "Mangan", "Pelling", "Rangpo"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli"],
            "Telangana": ["Hyderabad", "Warangal", "Khammam", "Karimnagar", "Nizamabad"],
            "Tripura": ["Agartala", "Udaipur", "Kailashahar", "Sabroom", "Belonia"],
            "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Allahabad"],
            "Uttarakhand": ["Dehradun", "Nainital", "Haridwar", "Rishikesh", "Roorkee"],
            "West Bengal": ["Kolkata", "Darjeeling", "Siliguri", "Asansol", "Howrah"],
            "Andaman and Nicobar Islands": ["Port Blair", "Car Nicobar", "Havelock", "Neil Island", "Diglipur"],
            "Chandigarh": ["Chandigarh"],
            "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu", "Silvassa"],
            "Lakshadweep": ["Kavaratti", "Minicoy", "Andrott"],
            "Delhi": ["New Delhi", "Chandni Chowk", "Connaught Place", "Lajpat Nagar", "Dwarka"],
            "Puducherry": ["Puducherry", "Karaikal", "Mahe", "Yanam"]
        }
        self.map_window = None
        self.setup_ui()

    def setup_ui(self):
        name_label = tk.Label(self.window, text="Skycast Weather Forecast Application", font=("Time New Roman", 18, "bold"))
        name_label.place(x=50, y=50, height=50, width=450)

        self.state_name = tk.StringVar()
        
        state_list_name = list(self.city_coordinates.keys())
        self.state_combo_box = ttk.Combobox(self.window, justify='center', values=state_list_name, font=("Time New Roman", 15, "bold"), textvariable=self.state_name)
        self.state_combo_box.place(x=50, y=120, height=50, width=450)

        self.city_list_name = tk.StringVar()
        self.city_combo_box = ttk.Combobox(self.window, justify='center', values=[], font=("Time New Roman", 15, "bold"), textvariable=self.city_list_name)
        self.city_combo_box.place(x=50, y=195, height=50, width=450)

        self.state_combo_box.bind("<<ComboboxSelected>>", self.update_cities)

        # Left-side labels
        self.weather_label = tk.Label(self.window, text="Weather Climate", font=("Time New Roman", 10))
        self.weather_label.place(x=80, y=360, height=20, width=180)

        self.weather_description_label = tk.Label(self.window, text="Weather Description", font=("Time New Roman", 10))
        self.weather_description_label.place(x=80, y=390, height=20, width=180)

        self.temperature_label = tk.Label(self.window, text="Temperature", font=("Time New Roman", 10))
        self.temperature_label.place(x=80, y=420, height=20, width=180)

        self.pressure_label = tk.Label(self.window, text="Pressure", font=("Time New Roman", 10))
        self.pressure_label.place(x=80, y=450, height=20, width=180)

        # Data display labels
        self.weather_label1 = tk.Label(self.window, text="", font=("Time New Roman", 10))
        self.weather_label1.place(x=280, y=360, height=20, width=180)

        self.weather_description_label1 = tk.Label(self.window, text="", font=("Time New Roman", 10))
        self.weather_description_label1.place(x=280, y=390, height=20, width=180)

        self.temperature_label1 = tk.Label(self.window, text="", font=("Time New Roman", 10))
        self.temperature_label1.place(x=280, y=420, height=20, width=180)

        self.pressure_label1 = tk.Label(self.window, text="", font=("Time New Roman", 10))
        self.pressure_label1.place(x=280, y=450, height=20, width=180)

        # Buttons
        check_button = tk.Button(self.window, text="Check", font=("Time New Roman", 13, "bold"), command=self.data_get)
        check_button.place(x=110, y=280, height=50, width=100)

        refresh_button = tk.Button(self.window, text="Refresh", font=("Time New Roman", 13, "bold"), command=self.set_data)
        refresh_button.place(x=220, y=280, height=50, width=100)

        exit_button = tk.Button(self.window, text="Exit", font=("Time New Roman", 13, "bold"), command=self.window.quit)
        exit_button.place(x=330, y=280, height=50, width=100)

    def update_cities(self, event):
        selected_state = self.state_name.get()
        if selected_state in self.city_coordinates:
            self.city_combo_box['values'] = self.city_coordinates[selected_state]
        else:
            self.city_combo_box['values'] = []

    def data_get(self):
        city = self.city_combo_box.get()
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a4eabd1b7ebcd5848f79910cfb77b7a6").json()

        if data.get("cod") != 200:
            self.weather_label1.config(text="Error fetching data")
            self.weather_description_label1.config(text="")
            self.temperature_label1.config(text="")
            self.pressure_label1.config(text="")
            return

        self.weather_label1.config(text=data["weather"][0]["main"])
        self.weather_description_label1.config(text=data["weather"][0]["description"])
        self.temperature_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
        self.pressure_label1.config(text=data["main"]["pressure"])

        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        if self.map_window is None or not self.map_window.winfo_exists():
            self.open_map_window(lat, lon, city)

    def open_map_window(self, lat, lon, city):
        self.map_window = tk.Toplevel(self.window)
        self.map_window.geometry(f"{550}x{550}+770+120")
        self.map_window.title(f"Visualize Through Skycast Map: {city}")

        map_widget = tkintermapview.TkinterMapView(self.map_window, width=550, height=550, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        map_widget.set_position(lat, lon)
        map_widget.set_zoom(10)

        marker = map_widget.set_position(lat, lon, marker=True)
        marker.set_text(city)

    def set_data(self):
        self.state_name.set("")
        self.city_combo_box.set("")
        self.weather_label1.config(text="")
        self.weather_description_label1.config(text="")
        self.temperature_label1.config(text="")
        self.pressure_label1.config(text="")

        if self.map_window is not None and self.map_window.winfo_exists():
            self.map_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SkycastApp(root)
    root.mainloop()