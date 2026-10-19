# File main chay chuong trinh chinh (CLI)
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from services import QuanLyKhachSan
from models import PhongThuong, PhongVIP

def in_menu():
    print("\n" + "=" * 40)
    print("    HE THONG QUAN LY KHACH SAN (CLI)   ")
    print("=" * 40)
    print("1. Hien thi danh sach phong")
    print("2. Them phong moi")
    print("3. Dat phong")
    print("4. Tra phong & Thanh toan")
    print("5. Xem bao cao doanh thu")
    print("6. Thoat & Luu du lieu")
    print("=" * 40)

def main():
    # Khoi tao quan ly (tu dong nap du lieu cu neu co)
    ql = QuanLyKhachSan()

    while True:
        in_menu()
        chon = input("Nhap lua chon cua ban (1-6): ").strip()

        # Xu ly chuc nang 1: Hien thi danh sach phong
        if chon == "1":
            ql.hien_thi_phong()

        # Xu ly chuc nang 2: Them phong moi
        elif chon == "2":
            print("\n--- THEM PHONG MOI ---")
            ma_phong = input("Nhap ma phong: ").strip()
            if not ma_phong:
                print("Loi: Ma phong khong duoc de trong!")
                continue

            ten_phong = input("Nhap ten phong: ").strip()

            # Bat loi nhap chu o gia tien
            try:
                gia_co_ban = float(input("Nhap gia phong co ban (VND): "))
                if gia_co_ban <= 0:
                    print("Loi: Gia phong phai lon hon 0!")
                    continue
            except ValueError:
                print("Loi: Gia tien phai la so, khong duoc nhap chu!")
                continue

            loai = input("Chon loai phong (1: Thuong, 2: VIP): ").strip()
            if loai == "1":
                phong_moi = PhongThuong(ma_phong, ten_phong, gia_co_ban)
                ql.them_phong(phong_moi)
            elif loai == "2":
                # Neu chon VIP thi nhap them cac phi phu thu
                try:
                    phi_don_dep = float(input("Nhap phi don dep (VND): "))
                    phi_minibar = float(input("Nhap phi minibar (VND): "))
                except ValueError:
                    print("Loi: Phi dich vu phai la so!")
                    continue
                phong_moi = PhongVIP(ma_phong, ten_phong, gia_co_ban, phi_don_dep, phi_minibar)
                ql.them_phong(phong_moi)
            else:
                print("Loi: Lua chon loai phong khong hop le (chi chon 1 hoac 2)!")

        # Xu ly chuc nang 3: Dat phong
        elif chon == "3":
            print("\n--- DAT PHONG ---")
            ma_phong = input("Nhap ma phong can dat: ").strip()
            ma_khach = input("Nhap ma khach hang: ").strip()
            ten_khach = input("Nhap ho ten khach: ").strip()
            cccd = input("Nhap so CCCD/CMND: ").strip()

            # Bat loi nhap so ngay thue
            try:
                so_ngay = int(input("Nhap so ngay thue: "))
                if so_ngay <= 0:
                    print("Loi: So ngay thue phai lon hon 0!")
                    continue
            except ValueError:
                print("Loi: So ngay thue phai la so nguyen, khong duoc nhap chu!")
                continue

            # Goi ham dat phong trong service (ham se check ma phong co ton tai va con trong hay khong)
            ql.dat_phong(ma_phong, ma_khach, ten_khach, cccd, so_ngay)

        # Xu ly chuc nang 4: Tra phong & Thanh toan
        elif chon == "4":
            print("\n--- TRA PHONG & THANH TOAN ---")
            ma_phong = input("Nhap ma phong can tra: ").strip()
            ql.tra_phong(ma_phong)

        # Xu ly chuc nang 5: Xem bao cao doanh thu
        elif chon == "5":
            ql.bao_cao_doanh_thu()

        # Xu ly chuc nang 6: Thoat va luu du lieu
        elif chon == "6":
            ql.luu_du_lieu()
            print("Cam on ban da su dung phan mem! Tam biet.")
            break

        # Truong hop nguoi dung nhap lua chon khac 1-6
        else:
            print("Loi: Lua chon khong hop le, vui long chi nhap tu 1 den 6!")

if __name__ == "__main__":
    main()
