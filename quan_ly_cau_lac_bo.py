import json
from datetime import datetime

# ==============================
# KHAI BAO DU LIEU
# ==============================

ds_thanh_vien = []
lich_su_dong_phi = []

TEN_FILE = "cau_lac_bo.txt"


# ==============================
# CAC HAM KIEM TRA DU LIEU
# ==============================

def kiem_tra_ngay(ngay):
    try:
        datetime.strptime(ngay, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def kiem_tra_ma(ma):
    for tv in ds_thanh_vien:
        if tv["ma"] == ma:
            return True
    return False


def tim_thanh_vien(ma):
    for tv in ds_thanh_vien:
        if tv["ma"] == ma:
            return tv
    return None


def tinh_hoi_phi(loai):
    if loai == "Thuong":
        return 100000
    elif loai == "Tich cuc":
        return 150000
    elif loai == "Ban chu nhiem":
        return 200000
    else:
        return 0


def nhap_ngay(thong_bao):
    while True:
        ngay = input(thong_bao)

        if kiem_tra_ngay(ngay):
            return ngay

        print("Ngay khong hop le! Nhap theo dd/mm/yyyy.")


def nhap_so_dien_thoai():
    while True:
        sdt = input("Nhap so dien thoai: ").strip()

        if sdt.isdigit() and 10 <= len(sdt) <= 11:
            return sdt

        print("So dien thoai phai co 10 hoac 11 chu so!")


def nhap_loai_thanh_vien():
    while True:
        print("1. Thuong")
        print("2. Tich cuc")
        print("3. Ban chu nhiem")

        chon = input("Chon loai thanh vien: ")

        if chon == "1":
            return "Thuong"
        elif chon == "2":
            return "Tich cuc"
        elif chon == "3":
            return "Ban chu nhiem"
        else:
            print("Lua chon khong hop le!")


# ==============================
# 1. THEM THANH VIEN
# ==============================

def them_thanh_vien():
    print("\n--- THEM THANH VIEN ---")

    ma = input("Nhap ma thanh vien: ").strip()

    if ma == "":
        print("Ma thanh vien khong duoc bo trong!")
        return

    if kiem_tra_ma(ma):
        print("Ma thanh vien da ton tai!")
        return

    ho_ten = input("Nhap ho ten: ").strip()

    if ho_ten == "":
        print("Ho ten khong duoc bo trong!")
        return

    ngay_sinh = nhap_ngay("Nhap ngay sinh: ")

    gioi_tinh = input("Nhap gioi tinh: ").strip()

    sdt = nhap_so_dien_thoai()

    ngay_gia_nhap = nhap_ngay("Nhap ngay gia nhap: ")

    loai = nhap_loai_thanh_vien()

    hoi_phi = tinh_hoi_phi(loai)

    # Tao dictionary thanh vien
    tv = {
        "ma": ma,
        "ho_ten": ho_ten,
        "ngay_sinh": ngay_sinh,
        "gioi_tinh": gioi_tinh,
        "sdt": sdt,
        "ngay_gia_nhap": ngay_gia_nhap,
        "loai": loai,
        "hoi_phi": hoi_phi,
        "trang_thai": "Chua dong"
    }

    ds_thanh_vien.append(tv)

    print("Them thanh vien thanh cong!")


# ==============================
# 2. HIEN THI DANH SACH
# ==============================

def hien_thi_danh_sach():
    print("\n--- DANH SACH THANH VIEN ---")

    if len(ds_thanh_vien) == 0:
        print("Danh sach thanh vien rong!")
        return

    for tv in ds_thanh_vien:
        print("--------------------------------")
        print("Ma thanh vien:", tv["ma"])
        print("Ho ten:", tv["ho_ten"])
        print("Ngay sinh:", tv["ngay_sinh"])
        print("Gioi tinh:", tv["gioi_tinh"])
        print("So dien thoai:", tv["sdt"])
        print("Ngay gia nhap:", tv["ngay_gia_nhap"])
        print("Loai thanh vien:", tv["loai"])
        print("Hoi phi:", tv["hoi_phi"], "dong")
        print("Trang thai:", tv["trang_thai"])


# ==============================
# 3. CAP NHAT THANH VIEN
# ==============================

def cap_nhat_thanh_vien():
    print("\n--- CAP NHAT THANH VIEN ---")

    ma = input("Nhap ma thanh vien can cap nhat: ").strip()

    tv = tim_thanh_vien(ma)

    if tv is None:
        print("Khong tim thay thanh vien!")
        return

    print("Nhap thong tin moi.")
    print("Neu muon giu thong tin cu, nhan Enter.")

    ho_ten = input("Ho ten moi: ").strip()

    if ho_ten != "":
        tv["ho_ten"] = ho_ten

    ngay_sinh = input("Ngay sinh moi (dd/mm/yyyy): ").strip()

    if ngay_sinh != "":
        if kiem_tra_ngay(ngay_sinh):
            tv["ngay_sinh"] = ngay_sinh
        else:
            print("Ngay sinh khong hop le, giu ngay cu.")

    gioi_tinh = input("Gioi tinh moi: ").strip()

    if gioi_tinh != "":
        tv["gioi_tinh"] = gioi_tinh

    sdt = input("So dien thoai moi: ").strip()

    if sdt != "":
        if sdt.isdigit() and 10 <= len(sdt) <= 11:
            tv["sdt"] = sdt
        else:
            print("So dien thoai khong hop le, giu so cu.")

    ngay = input("Ngay gia nhap moi: ").strip()

    if ngay != "":
        if kiem_tra_ngay(ngay):
            tv["ngay_gia_nhap"] = ngay
        else:
            print("Ngay gia nhap khong hop le, giu ngay cu.")

    print("Chon loai thanh vien moi:")
    print("1. Thuong")
    print("2. Tich cuc")
    print("3. Ban chu nhiem")
    print("Nhan Enter de giu loai cu.")

    chon = input("Lua chon: ")

    if chon == "1":
        tv["loai"] = "Thuong"
    elif chon == "2":
        tv["loai"] = "Tich cuc"
    elif chon == "3":
        tv["loai"] = "Ban chu nhiem"

    # Cap nhat hoi phi theo loai moi
    tv["hoi_phi"] = tinh_hoi_phi(tv["loai"])

    print("Cap nhat thanh cong!")


# ==============================
# 4. XOA THANH VIEN
# ==============================

def xoa_thanh_vien():
    print("\n--- XOA THANH VIEN ---")

    ma = input("Nhap ma thanh vien can xoa: ").strip()

    tv = tim_thanh_vien(ma)

    if tv is None:
        print("Khong tim thay thanh vien!")
        return

    xac_nhan = input("Ban co chac chan muon xoa? (y/n): ")

    if xac_nhan.lower() == "y":
        ds_thanh_vien.remove(tv)

        # Xoa lich su dong phi cua thanh vien
        for ls in lich_su_dong_phi[:]:
            if ls["ma"] == ma:
                lich_su_dong_phi.remove(ls)

        print("Xoa thanh vien thanh cong!")
    else:
        print("Da huy thao tac xoa.")


# ==============================
# 5. TIM KIEM THANH VIEN
# ==============================

def tim_kiem():
    print("\n--- TIM KIEM THANH VIEN ---")
    print("1. Tim theo ma")
    print("2. Tim theo ho ten")
    print("3. Tim theo so dien thoai")
    print("4. Tim theo loai thanh vien")

    chon = input("Lua chon: ")

    ket_qua = []

    if chon == "1":
        ma = input("Nhap ma thanh vien: ").strip()

        tv = tim_thanh_vien(ma)

        if tv is not None:
            ket_qua.append(tv)

    elif chon == "2":
        ten = input("Nhap ho ten can tim: ").strip().lower()

        for tv in ds_thanh_vien:
            if ten in tv["ho_ten"].lower():
                ket_qua.append(tv)

    elif chon == "3":
        sdt = input("Nhap so dien thoai: ").strip()

        for tv in ds_thanh_vien:
            if tv["sdt"] == sdt:
                ket_qua.append(tv)

    elif chon == "4":
        loai = nhap_loai_thanh_vien()

        for tv in ds_thanh_vien:
            if tv["loai"] == loai:
                ket_qua.append(tv)

    else:
        print("Lua chon khong hop le!")
        return

    if len(ket_qua) == 0:
        print("Khong tim thay thanh vien!")
    else:
        for tv in ket_qua:
            print(tv)


# ==============================
# 6. SAP XEP THANH VIEN
# ==============================

def sap_xep():
    print("\n--- SAP XEP THANH VIEN ---")
    print("1. Sap xep theo ho ten")
    print("2. Sap xep theo hoi phi")
    print("3. Sap xep theo ngay gia nhap")

    chon = input("Lua chon: ")

    if chon == "1":
        khoa = "ho_ten"

    elif chon == "2":
        khoa = "hoi_phi"

    elif chon == "3":
        khoa = "ngay_gia_nhap"

    else:
        print("Lua chon khong hop le!")
        return

    print("1. Tang dan")
    print("2. Giam dan")

    chieu = input("Chon chieu sap xep: ")

    if chieu == "1":
        tang = True
    elif chieu == "2":
        tang = False
    else:
        print("Lua chon khong hop le!")
        return

    # Sap xep ngay theo nam, thang, ngay
    if khoa == "ngay_gia_nhap":
        ds_thanh_vien.sort(
            key=lambda tv: datetime.strptime(
                tv[khoa], "%d/%m/%Y"
            ),
            reverse=not tang
        )
    else:
        ds_thanh_vien.sort(
            key=lambda tv: tv[khoa],
            reverse=not tang
        )

    print("Sap xep thanh cong!")
    hien_thi_danh_sach()


# ==============================
# 7. THU HOI PHI
# ==============================


def thu_hoi_phi():
    print("\n--- THU HOI PHI ---")

    ma = input("Nhap ma thanh vien: ").strip()
    tv = tim_thanh_vien(ma)

    if tv is None:
        print("Thanh vien khong ton tai!")
        return

    ky = input("Nhap ky dong phi (vd: 10/2026): ").strip()

    try:
        datetime.strptime(ky, "%m/%Y")
    except ValueError:
        print("Ky dong phi khong hop le! Nhap MM/YYYY.")
        return

    # Kiem tra giao dich da ton tai
    for ls in lich_su_dong_phi:
        if ls["ma"] == ma and ls["ky"] == ky:
            # Dong bo lai trang thai thanh vien
            tv["trang_thai"] = "Da dong"
            luu_du_lieu()

            print("Thanh vien da dong phi ky nay!")
            print("Trang thai da duoc cap nhat: Da dong")
            print("Du lieu da duoc luu vao file.")
            return

    so_tien = tinh_hoi_phi(tv["loai"])

    print("Thanh vien:", tv["ho_ten"])
    print("Loai thanh vien:", tv["loai"])
    print("Hoi phi phai dong:", so_tien, "dong")

    xac_nhan = input("Xac nhan thu phi? (y/n): ").strip()

    if xac_nhan.lower() == "y":
        lich_su_dong_phi.append({
            "ma": ma,
            "ky": ky,
            "so_tien": so_tien
        })

        tv["trang_thai"] = "Da dong"

        # Luu ngay sau khi thu phi
        luu_du_lieu()

        print("Thu hoi phi thanh cong!")
        print("Trang thai: Da dong")
        print("Giao dich da duoc luu vao file.")
    else:
        print("Da huy thao tac thu phi.")

# ==============================
# 8. THONG KE
# ==============================

def thong_ke():
    print("\n--- THONG KE ---")

    tong_tv = len(ds_thanh_vien)

    da_dong = 0
    chua_dong = 0

    for tv in ds_thanh_vien:
        if tv["trang_thai"] == "Da dong":
            da_dong += 1
        else:
            chua_dong += 1

    tong_tien = 0

    for ls in lich_su_dong_phi:
        tong_tien += ls["so_tien"]

    # Dem thanh vien theo loai
    thuong = 0
    tich_cuc = 0
    ban_chu_nhiem = 0

    for tv in ds_thanh_vien:
        if tv["loai"] == "Thuong":
            thuong += 1
        elif tv["loai"] == "Tich cuc":
            tich_cuc += 1
        elif tv["loai"] == "Ban chu nhiem":
            ban_chu_nhiem += 1

    print("Tong so thanh vien:", tong_tv)
    print("So thanh vien da dong phi:", da_dong)
    print("So thanh vien chua dong phi:", chua_dong)
    print("Tong hoi phi da thu:", tong_tien, "dong")

    print("Thanh vien loai Thuong:", thuong)
    print("Thanh vien loai Tich cuc:", tich_cuc)
    print("Thanh vien Ban chu nhiem:", ban_chu_nhiem)



# ==============================
# 9. LUU DU LIEU
# ==============================

def luu_du_lieu():
    try:
        # Gop danh sach thanh vien va lich su vao file
        du_lieu = {
            "thanh_vien": ds_thanh_vien,
            "lich_su": lich_su_dong_phi
        }

        with open(TEN_FILE, "w", encoding="utf-8") as f:
            json.dump(
                du_lieu,
                f,
                ensure_ascii=False,
                indent=4
            )

        print("Luu du lieu thanh cong!")

    except OSError:
        print("Khong the ghi file!")


# ==============================
# 10. DOC DU LIEU
# ==============================

def doc_du_lieu():
    try:
        with open(TEN_FILE, "r", encoding="utf-8") as f:
            du_lieu = json.load(f)

        # Kiem tra du lieu co dung cau truc khong
        thanh_vien_moi = du_lieu["thanh_vien"]
        lich_su_moi = du_lieu["lich_su"]

        if not isinstance(thanh_vien_moi, list):
            raise ValueError("Danh sach thanh vien khong hop le")

        if not isinstance(lich_su_moi, list):
            raise ValueError("Lich su dong phi khong hop le")

        ds_thanh_vien.clear()
        ds_thanh_vien.extend(thanh_vien_moi)

        lich_su_dong_phi.clear()
        lich_su_dong_phi.extend(lich_su_moi)

        print("Doc du lieu thanh cong!")

    except FileNotFoundError:
        print("File chua ton tai. Hay them thanh vien moi!")

    except (OSError, json.JSONDecodeError, ValueError, KeyError):
        print("File bi loi hoac sai cau truc!")


# ==============================
# MENU CHINH
# ==============================

def menu():
    while True:
        print("\n========================================")
        print("       QUAN LY CAU LAC BO")
        print("========================================")
        print("1. Them thanh vien")
        print("2. Hien thi danh sach")
        print("3. Cap nhat thanh vien")
        print("4. Xoa thanh vien")
        print("5. Tim kiem")
        print("6. Sap xep")
        print("7. Thu hoi phi")
        print("8. Thong ke")
        print("9. Luu du lieu")
        print("10. Doc du lieu")
        print("0. Thoat")
        print("========================================")

        try:
            chon = int(input("Lua chon: "))

            if chon == 1:
                them_thanh_vien()

            elif chon == 2:
                hien_thi_danh_sach()

            elif chon == 3:
                cap_nhat_thanh_vien()

            elif chon == 4:
                xoa_thanh_vien()

            elif chon == 5:
                tim_kiem()

            elif chon == 6:
                sap_xep()

            elif chon == 7:
                thu_hoi_phi()

            elif chon == 8:
                thong_ke()

            elif chon == 9:
                luu_du_lieu()

            elif chon == 10:
                doc_du_lieu()

            elif chon == 0:
                luu_du_lieu()
                print("Cam on ban da su dung chuong trinh!")
                break

            else:
                print("Vui long chon tu 0 den 10!")

        except ValueError:
            print("Vui long nhap so nguyen!")


# ==============================
# CHAY CHUONG TRINH
# ==============================

# Tu dong doc du lieu khi khoi dong
doc_du_lieu()

# Hien menu
menu()