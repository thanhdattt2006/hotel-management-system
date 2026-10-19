import json
from models import PhongThuong, PhongVIP, KhachHang, PhieuThue

# File luu du lieu mac dinh
FILE_NAME = "khachsan_data.json"

# Ham luu du lieu ra file json
def save_data(ds_phong, ds_phieu, tong_doanh_thu=0):
    data = {
        "tong_doanh_thu": tong_doanh_thu,
        "danh_sach_phong": [],
        "danh_sach_phieu": []
    }

    # Luu danh sach phong
    for p in ds_phong:
        p_dict = {
            "ma_phong": p.ma_phong,
            "ten_phong": p.ten_phong,
            "gia_co_ban": p.gia_co_ban,
            "trang_thai": p.get_trang_thai()
        }
        if isinstance(p, PhongVIP):
            p_dict["loai"] = "VIP"
            p_dict["phi_don_dep"] = p.phi_don_dep
            p_dict["phi_minibar"] = p.phi_minibar
        else:
            p_dict["loai"] = "Thuong"
        data["danh_sach_phong"].append(p_dict)

    # Luu danh sach phieu thue
    for phieu in ds_phieu:
        phieu_dict = {
            "khach_hang": {
                "ma_khach": phieu.khach_hang.ma_khach,
                "ten": phieu.khach_hang.ten,
                "cccd": phieu.khach_hang.cccd
            },
            "ma_phong": phieu.phong.ma_phong,
            "so_ngay_thue": phieu.so_ngay_thue
        }
        data["danh_sach_phieu"].append(phieu_dict)

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("-> Luu du lieu thanh cong vao file " + FILE_NAME)
    except Exception as e:
        print("Loi khi luu file: ", e)


# Ham doc du lieu tu file json
def load_data():
    ds_phong = []
    ds_phieu = []
    tong_doanh_thu = 0

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            tong_doanh_thu = data.get("tong_doanh_thu", 0)

            # Khoi phuc danh sach phong
            for p_dict in data.get("danh_sach_phong", []):
                if p_dict.get("loai") == "VIP":
                    p = PhongVIP(
                        p_dict["ma_phong"],
                        p_dict["ten_phong"],
                        p_dict["gia_co_ban"],
                        p_dict.get("phi_don_dep", 50000),
                        p_dict.get("phi_minibar", 100000),
                        p_dict.get("trang_thai", "Trống")
                    )
                else:
                    p = PhongThuong(
                        p_dict["ma_phong"],
                        p_dict["ten_phong"],
                        p_dict["gia_co_ban"],
                        p_dict.get("trang_thai", "Trống")
                    )
                ds_phong.append(p)

            # Khoi phuc danh sach phieu thue
            for phieu_dict in data.get("danh_sach_phieu", []):
                kh_dict = phieu_dict["khach_hang"]
                kh = KhachHang(kh_dict["ma_khach"], kh_dict["ten"], kh_dict["cccd"])

                # Tim phong tuong ung theo ma_phong
                phong_tim_thay = None
                for p in ds_phong:
                    if p.ma_phong == phieu_dict["ma_phong"]:
                        phong_tim_thay = p
                        break

                if phong_tim_thay:
                    phieu = PhieuThue(kh, phong_tim_thay, phieu_dict["so_ngay_thue"])
                    ds_phieu.append(phieu)

    except FileNotFoundError:
        # Neu chua co file thi khong bi loi crash
        print("Chua co file du lieu cu, he thong se tao moi khi luu.")
    except Exception as e:
        print("Co loi khi doc file: ", e)

    return ds_phong, ds_phieu, tong_doanh_thu
