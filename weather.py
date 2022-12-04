from tkinter import *
from tkinter import ttk #combobox
import requests #to use apis



def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()

    w1.config(text=data["weather"][0]["main"])
    wd1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"]-273)))
    p1.config(text=data["main"]["pressure"])




win = Tk()
win.title("weather")
win.config(bg="blue")
win.geometry("500x600")

city_name = StringVar()

name = Label(win,text="MY WEATHER APP",font=("Time New Roman",30,"bold"))
name.place(x=25, y=50,height=50,width=450)

#combobox for all cities
#list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

list_name = ['Kolhapur', 'Port Blair', 'Adilabad', 'Adoni', 'Amadalavalasa', 'Amalapuram', 'Anakapalle', 'Anantapur', 'Badepalle', 'Banganapalle', 'Bapatla', 'Bellampalle', 'Bethamcherla', 'Bhadrachalam', 'Bhainsa', 'Bheemunipatnam', 'Bhimavaram', 'Bhongir', 'Bobbili', 'Bodhan', 'Chilakaluripet', 'Chirala', 'Chittoor', 'Cuddapah', 'Devarakonda', 'Dharmavaram', 'Eluru', 'Farooqnagar', 'Gadwal', 'Gooty', 'Gudivada', 'Gudur', 'Guntakal', 'Guntur', 'Hanuman Junction', 'Hindupur', 'Hyderabad', 'Ichchapuram', 'Jaggaiahpet', 'Jagtial', 'Jammalamadugu', 'Jangaon', 'Kadapa', 'Kadiri', 'Kagaznagar', 'Kakinada', 'Kalyandurg', 'Kamareddy', 'Kandukur', 'Karimnagar', 'Kavali', 'Khammam', 'Koratla', 'Kothagudem', 'Kothapeta', 'Kovvur', 'Kurnool', 'Kyathampalle', 'Macherla', 'Machilipatnam', 'Madanapalle', 'Mahbubnagar', 'Mancherial', 'Mandamarri', 'Mandapeta', 'Manuguru', 'Markapur', 'Medak', 'Miryalaguda', 'Mogalthur', 'Nagari', 'Nagarkurnool', 'Nandyal', 'Narasapur', 'Narasaraopet', 'Narayanpet', 'Narsipatnam', 'Nellore', 'Nidadavole', 'Nirmal', 'Nizamabad', 'Nuzvid', 'Ongole', 'Palacole', 'Palasa Kasibugga', 'Palwancha', 'Parvathipuram', 'Pedana', 'Peddapuram', 'Pithapuram', 'Pondur', 'Ponnur', 'Proddatur', 'Punganur', 'Puttur', 'Rajahmundry', 'Rajam', 'Ramachandrapuram', 'Ramagundam', 'Rayachoti', 'Rayadurg', 'Renigunta', 'Repalle', 'Sadasivpet', 'Salur', 'Samalkot', 'Sangareddy', 'Sattenapalle', 'Siddipet', 'Singapur', 'Sircilla', 'Srikakulam', 'Srikalahasti', 'Suryapet', 'Tadepalligudem', 'Tadpatri', 'Tandur', 'Tanuku', 'Tenali', 'Tirupati', 'Tuni', 'Uravakonda', 'Venkatagiri', 'Vicarabad', 'Vijayawada', 'Vinukonda', 'Visakhapatnam', 'Vizianagaram', 'Wanaparthy', 'Warangal', 'Yellandu', 'Yemmiganur', 'Yerraguntla', 'Zahirabad', 'Rajampet', 'Along', 'Bomdila', 'Itanagar', 'Naharlagun', 'Pasighat', 'Abhayapuri', 'Amguri', 'Anandnagaar', 'Barpeta', 'Barpeta Road', 'Bilasipara', 'Bongaigaon', 'Dhekiajuli', 'Dhubri', 'Dibrugarh', 'Digboi', 'Diphu', 'Dispur', 'Gauripur', 'Goalpara', 'Golaghat', 'Guwahati', 'Haflong', 'Hailakandi', 'Hojai', 'Jorhat', 'Karimganj', 'Kokrajhar', 'Lanka', 'Lumding', 'Mangaldoi', 'Mankachar', 'Margherita', 'Mariani', 'Marigaon', 'Nagaon', 'Nalbari', 'North Lakhimpur', 'Rangia', 'Sibsagar', 'Silapathar', 'Silchar', 'Tezpur', 'Tinsukia', 'Amarpur', 'Araria', 'Areraj', 'Arrah', 'Asarganj', 'Aurangabad', 'Bagaha', 'Bahadurganj', 'Bairgania', 'Bakhtiarpur', 'Banka', 'Banmankhi Bazar', 'Barahiya', 'Barauli', 'Barbigha', 'Barh', 'Begusarai', 'Behea', 'Bettiah', 'Bhabua', 'Bhagalpur', 'Bihar Sharif', 'Bikramganj', 'Bodh Gaya', 'Buxar', 'Chandan Bara', 'Chanpatia', 'Chhapra', 'Colgong', 'Dalsinghsarai', 'Darbhanga', 'Daudnagar', 'Dehri-on-Sone', 'Dhaka', 'Dighwara', 'Dumraon', 'Fatwah', 'Forbesganj', 'Gaya', 'Gogri Jamalpur', 'Gopalganj', 'Hajipur', 'Hilsa', 'Hisua', 'Islampur', 'Jagdispur', 'Jamalpur', 'Jamui', 'Jehanabad', 'Jhajha', 'Jhanjharpur', 'Jogabani', 'Kanti', 'Katihar', 'Khagaria', 'Kharagpur', 'Kishanganj', 'Lakhisarai', 'Lalganj', 'Madhepura', 'Madhubani', 'Maharajganj', 'Mahnar Bazar', 'Makhdumpur', 'Maner', 'Manihari', 'Marhaura', 'Masaurhi', 'Mirganj', 'Mokameh', 'Motihari', 'Motipur', 'Munger', 'Murliganj', 'Muzaffarpur', 'Narkatiaganj', 'Naugachhia', 'Nawada', 'Nokha', 'Patna', 'Piro', 'Purnia', 'Rafiganj', 'Rajgir', 'Ramnagar', 'Raxaul Bazar', 'Revelganj', 'Rosera', 'Saharsa', 'Samastipur', 'Sasaram', 'Sheikhpura', 'Sheohar', 'Sherghati', 'Silao', 'Sitamarhi', 'Siwan', 'Sonepur', 'Sugauli', 'Sultanganj', 'Supaul', 'Warisaliganj', 'Ahiwara', 'Akaltara', 'Ambagarh Chowki', 'Ambikapur', 'Arang', 'Bade Bacheli', 'Balod', 'Baloda Bazar', 'Bemetra', 'Bhatapara', 'Bilaspur', 'Birgaon', 'Champa', 'Chirmiri', 'Dalli-Rajhara', 'Dhamtari', 'Dipka', 'Dongargarh', 'Durg-Bhilai Nagar', 'Gobranawapara', 'Jagdalpur', 'Janjgir', 'Jashpurnagar', 'Kanker', 'Kawardha', 'Kondagaon', 'Korba', 'Mahasamund', 'Mahendragarh', 'Mungeli', 'Naila Janjgir', 'Raigarh', 'Raipur', 'Rajnandgaon', 'Sakti', 'Tilda Newra', 'Amli', 'Silvassa', 'Daman and Diu', 'Asola', 'Delhi', 'Aldona', 'Curchorem Cacora', 'Madgaon', 'Mapusa', 'Margao', 'Marmagao', 'Panaji', 'Ahmedabad', 'Amreli', 'Anand', 'Ankleshwar', 'Bharuch', 'Bhavnagar', 'Bhuj', 'Cambay', 'Dahod', 'Deesa', 'Dharampur', 'Dholka', 'Gandhinagar', 'Godhra', 'Himatnagar', 'Idar', 'Jamnagar', 'Junagadh', 'Kadi', 'Kalavad', 'Kalol', 'Kapadvanj', 'Karjan', 'Keshod', 'Khambhalia', 'Khambhat', 'Kheda', 'Khedbrahma', 'Kheralu', 'Kodinar', 'Lathi', 'Limbdi', 'Lunawada', 'Mahesana', 'Mahuva', 'Manavadar', 'Mandvi', 'Mangrol', 'Mansa', 'Mehmedabad', 'Modasa', 'Morvi', 'Nadiad', 'Navsari', 'Padra', 'Palanpur', 'Palitana', 'Pardi', 'Patan', 'Petlad', 'Porbandar', 'Radhanpur', 'Rajkot', 'Rajpipla', 'Rajula', 'Ranavav', 'Rapar', 'Salaya', 'Sanand', 'Savarkundla', 'Sidhpur', 'Sihor', 'Songadh', 'Surat', 'Talaja', 'Thangadh', 'Tharad', 'Umbergaon', 'Umreth', 'Una', 'Unjha', 'Upleta', 'Vadnagar', 'Vadodara', 'Valsad', 'Vapi', 'Veraval', 'Vijapur', 'Viramgam', 'Visnagar', 'Vyara', 'Wadhwan', 'Wankaner', 'Adalaj', 'Adityana', 'Alang', 'Ambaji', 'Ambaliyasan', 'Andada', 'Anjar', 'Anklav', 'Antaliya', 'Arambhada', 'Atul', 'Ballabhgarh', 'Ambala', 'Asankhurd', 'Assandh', 'Ateli', 'Babiyal', 'Bahadurgarh', 'Barwala', 'Bhiwani', 'Charkhi Dadri', 'Cheeka', 'Ellenabad 2', 'Faridabad', 'Fatehabad', 'Ganaur', 'Gharaunda', 'Gohana', 'Gurgaon', 'Haibat(Yamuna Nagar)', 'Hansi', 'Hisar', 'Hodal', 'Jhajjar', 'Jind', 'Kaithal', 'Kalan Wali', 'Kalka', 'Karnal', 'Ladwa', 'Mandi Dabwali', 'Narnaul', 'Narwana', 'Palwal', 'Panchkula', 'Panipat', 'Pehowa', 'Pinjore', 'Rania', 'Ratia', 'Rewari', 'Rohtak', 'Safidon', 'Samalkha', 'Shahbad', 'Sirsa', 'Sohna', 'Sonipat', 'Taraori', 'Thanesar', 'Tohana', 'Yamunanagar', 'Arki', 'Baddi', 'Bilaspur', 'Chamba', 'Dalhousie', 'Dharamsala', 'Hamirpur', 'Mandi', 'Nahan', 'Shimla', 'Solan', 'Sundarnagar', 'Jammu', 'Achabbal', 'Akhnoor', 'Anantnag', 'Arnia', 'Awantipora', 'Bandipore', 'Baramula', 'Kathua', 'Leh', 'Punch', 'Rajauri', 'Sopore', 'Srinagar', 'Udhampur', 'Amlabad', 'Ara', 'Barughutu', 'Bokaro Steel "City"', 'Chaibasa', 'Chakradharpur', 'Chandrapura', 'Chatra', 'Chirkunda', 'Churi', 'Daltonganj', 'Deoghar', 'Dhanbad', 'Dumka', 'Garhwa', 'Ghatshila', 'Giridih', 'Godda', 'Gomoh', 'Gumia', 'Gumla', 'Hazaribag', 'Hussainabad', 'Jamshedpur', 'Jamtara', 'Jhumri Tilaiya', 'Khunti', 'Lohardaga', 'Madhupur', 'Mihijam', 'Musabani', 'Pakaur', 'Patratu', 'Phusro', 'Ramngarh', 'Ranchi', 'Sahibganj', 'Saunda', 'Simdega', 'Tenu Dam-cum- Kathhara', 'Arasikere', 'Bangalore', 'Belgaum', 'Bellary', 'Chamrajnagar', 'Chikkaballapur', 'Chintamani', 'Chitradurga', 'Gulbarga', 'Gundlupet', 'Hassan', 'Hospet', 'Hubli', 'Karkala', 'Karwar', 'Kolar', 'Kota', 'Lakshmeshwar', 'Lingsugur', 'Maddur', 'Madhugiri', 'Madikeri', 'Magadi', 'Mahalingpur', 'Malavalli', 'Malur', 'Mandya', 'Mangalore', 'Manvi', 'Mudalgi', 'Mudbidri', 'Muddebihal', 'Mudhol', 'Mulbagal', 'Mundargi', 'Mysore', 'Nanjangud', 'Pavagada', 'Puttur', 'Rabkavi Banhatti', 'Raichur', 'Ramanagaram', 'Ramdurg', 'Ranibennur', 'Robertson Pet', 'Ron', 'Sadalgi', 'Sagar', 'Sakleshpur', 'Sandur', 'Sankeshwar', 'Saundatti-Yellamma', 'Savanur', 'Sedam', 'Shahabad', 'Shahpur', 'Shiggaon', 'Shikapur', 'Shimoga', 'Shorapur', 'Shrirangapattana', 'Sidlaghatta', 'Sindgi', 'Sindhnur', 'Sira', 'Sirsi', 'Siruguppa', 'Srinivaspur', 'Talikota', 'Tarikere', 'Tekkalakota', 'Terdal', 'Tiptur', 'Tumkur', 'Udupi', 'Vijayapura', 'Wadi', 'Yadgir', 'Adoor', 'Akathiyoor', 'Alappuzha', 'Ancharakandy', 'Aroor', 'Ashtamichira', 'Attingal', 'Avinissery', 'Chalakudy', 'Changanassery', 'Chendamangalam', 'Chengannur', 'Cherthala', 'Cheruthazham', 'Chittur-Thathamangalam', 'Chockli', 'Erattupetta', 'Guruvayoor', 'Irinjalakuda', 'Kadirur', 'Kalliasseri', 'Kalpetta', 'Kanhangad', 'Kanjikkuzhi', 'Kannur', 'Kasaragod', 'Kayamkulam', 'Kochi', 'Kodungallur', 'Kollam', 'Koothuparamba', 'Kothamangalam', 'Kottayam', 'Kozhikode', 'Kunnamkulam', 'Malappuram', 'Mattannur', 'Mavelikkara', 'Mavoor', 'Muvattupuzha', 'Nedumangad', 'Neyyattinkara', 'Ottappalam', 'Palai', 'Palakkad', 'Panniyannur', 'Pappinisseri', 'Paravoor', 'Pathanamthitta', 'Payyannur', 'Peringathur', 'Perinthalmanna', 'Perumbavoor', 'Ponnani', 'Punalur', 'Quilandy', 'Shoranur', 'Taliparamba', 'Thiruvalla', 'Thiruvananthapuram', 'Thodupuzha', 'Thrissur', 'Tirur', 'Vadakara', 'Vaikom', 'Varkala', 'Kavaratti', 'Ashok Nagar', 'Balaghat', 'Betul', 'Bhopal', 'Burhanpur', 'Chhatarpur', 'Dabra', 'Datia', 'Dewas', 'Dhar', 'Fatehabad', 'Gwalior', 'Indore', 'Itarsi', 'Jabalpur', 'Katni', 'Kotma', 'Lahar', 'Lundi', 'Maharajpur', 'Mahidpur', 'Maihar', 'Malajkhand', 'Manasa', 'Manawar', 'Mandideep', 'Mandla', 'Mandsaur', 'Mauganj', 'Mhow Cantonment', 'Mhowgaon', 'Morena', 'Multai', 'Murwara', 'Nagda', 'Nainpur', 'Narsinghgarh', 'Neemuch', 'Nepanagar', 'Niwari', 'Nowgong', 'Nowrozabad', 'Pachore', 'Pali', 'Panagar', 'Pandhurna', 'Panna', 'Pasan', 'Pipariya', 'Pitha']
list_name.sort()

com = ttk.Combobox(win,text="MY WEATHER APP",values=list_name,font=("Time New Roman",25,"bold"),textvariable=city_name)
com.place(x=25,y=140,height=40,width=450)


w = Label(win,text="Weather Climate",font=("Time New Roman",20))
w.place(x=25, y=280,height=50,width=210)
w1 = Label(win,text="",font=("Time New Roman",20))
w1.place(x=250, y=280,height=50,width=210)


wd = Label(win,text="Weather Descrpn.",font=("Time New Roman",18))
wd.place(x=25, y=350,height=50,width=210)
wd1 = Label(win,text="",font=("Time New Roman",20))
wd1.place(x=250, y=350,height=50,width=210) 


temp = Label(win,text="Temperature",font=("Time New Roman",20))
temp.place(x=25, y=420,height=50,width=210)
temp1 = Label(win,text="",font=("Time New Roman",20))
temp1.place(x=250, y=420,height=50,width=210) 


p = Label(win,text="Pressure",font=("Time New Roman",20))
p.place(x=25, y=490,height=50,width=210)
p1 = Label(win,text="",font=("Time New Roman",20))
p1.place(x=250, y=490,height=50,width=210) 

done_button = Button(win,text="DONE",font=("Time New Roman",30,"bold"),command=data_get)
done_button.place(x=150,y=210,height=50,width=200)


win.mainloop()