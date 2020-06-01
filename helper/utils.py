import binascii
import math
import os
import random
import string
import time
import uuid
from datetime import datetime, timedelta
from math import sin, cos, radians, asin, sqrt

import pytz
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import crypto
from rest_framework.response import Response

class ErrorResponse:
    @staticmethod
    def build_serializer_error(serializer, status):
        return Response({"status": "error", "errors": serializer.errors}, status=status)

    @staticmethod
    def build_text_error(text, status):
        return Response({"status": "error", "errors": text}, status=status)


def random_profile_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'profile_images/' + filename


def random_coupon_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'coupon_images/' + filename


def random_venue_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'venue_images/' + filename


def random_product_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'product_image/' + filename


def random_venue_logo_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'logo/' + filename


def random_banner_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'banner/' + filename


def random_retailer_image_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'retailer_images/' + filename


def random_media_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'media/' + filename


def random_thumbnail_name(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(uuid.uuid4()) + extension
    return 'thumbnails/' + filename


def isDuplicateInArray(array):
    seen = set()

    for x in array:
        if x in seen:
            return True
        else:
            seen.add(x)

    return False


def calc_dist_fixed(lat1, lng1, lat2, lng2):
    """
    Calculate the great circle distance between two points on the earth (specified in decimal degrees)
    """
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    # haversine formula
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    A = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    C = 2 * asin(sqrt(A))
    R = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return round(C * R, 1)


def time_to_utc(naive, timezone='Asia/Kolkata'):
    local = pytz.timezone(timezone)
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt


def time_to_ist(naive, timezone='Asia/Kolkata'):
    ist_time = naive.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(timezone))
    # if utc.date() > ist_time.date():
    #     one_day = timedelta(days=1)
    #     ist_time += one_day
    return ist_time


def time_to_ist_time(naive, timezone='Asia/Kolkata'):
    # return pytz.timezone(timezone).localize(naive)
    naive = datetime.combine(datetime.now(), naive)
    return naive.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(timezone)).time()


def add_one_hour(naiveTime):
    naive_ = datetime.combine(datetime.now(), naiveTime) + timedelta(hours=1)
    return naive_.time()


def add_one_hour_to_date(naiveDate):
    naive_ = naiveDate + timedelta(hours=1)
    return naive_


def add_duration_to_date(naiveDate, sport_info_minutes):
    naive_ = naiveDate + timedelta(minutes=sport_info_minutes)
    return naive_


def get_datetime_from_time(naive, date):
    return datetime.combine(date, naive)


def readable_date_time(time):
    return time.strftime("%Y-%m-%d %H:%M")


def readable_time(time):
    return time.strftime("%H:%M")


def readable_date(time):
    return time.strftime("%Y-%m-%d")


def booking_date(time):
    return time.strftime("%Y%m%d")


def generate_invoice_number(invoice_prefix, last_invoice_id):
    total_len = invoice_prefix.__len__() + str(int(last_invoice_id.split(invoice_prefix)[1]) + 1).__len__()
    remaining_len = 12 - total_len
    inv_num = "{}{}{}".format(invoice_prefix, remaining_len * "0", int(last_invoice_id.split(invoice_prefix)[1]) + 1)
    return inv_num


def uniqid(prefix='', more_entropy=False):
    # todo change to six... 17031558c92bc
    m = time.time()
    uniqid = '%8x%05x' % (math.floor(m), (m - math.floor(m)) * 1000000)
    uniqid = uniqid[6:]
    if more_entropy:
        valid_chars = list(set(string.hexdigits.lower()))
        entropy_string = ''
        for i in range(0, 10, 1):
            entropy_string += random.choice(valid_chars)
        uniqid = uniqid + entropy_string
    uniqid = "{}{}".format(prefix, uniqid)
    return uniqid


def singlebooking_txt(booking):
    return render_to_string('sms/single_booking.txt',
                            {'sport': booking.sport.sport, 'court': booking.court, 'booking_id': booking.bookingID,
                             'booking_date': booking.slot.slot_from.date(), 'slot_from': booking.slot.slot_from.time(),
                             'slot_to': booking.slot.slot_to.time(), 'sport_center': booking.venue.venue_name})


def bulkbooking_txt(booking):
    return render_to_string('sms/bulk_booking.txt',
                            {'sport': booking.sport.sport, 'sport_center': booking.venue.venue_name})


def cancelbooking_txt(booking):
    return render_to_string('sms/cancel_booking.txt',
                            {'booking_id': booking.bookingID})


def canceladdonbooking_txt(booking):
    return render_to_string('sms/cancel_addon',
                            {'sport': booking.booking.sport.sport, 'sport_center': booking.booking.venue.venue_name})


def cancel_bulkbooking_txt(booking):
    template_name = 'sms/cancel_bulkbooking.txt'
    context = {'sport': booking.sport.sport, 'sport_center': booking.venue.venue_name}
    return render_to_string(template_name, context)


def setset_cookie(response, key, value, days_expire=700):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.strftime(
        datetime.utcnow() + timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires)


def generate_random_string(length=8, prefix='N', allowed_chars='0123456789'):
    str_ = crypto.get_random_string(length=length, allowed_chars=allowed_chars)
    if not prefix:
        return str_
    return prefix + str_


def generate_secret_key(strength=10):
    return binascii.hexlify(os.urandom(strength)).decode()


from datetime import date, timedelta


def get_first_day(dt, d_years=0, d_months=0):
    # d_years, d_months are "deltas" to apply to dt
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m - 1, 12)
    return date(y + a, m + 1, 1)


def get_last_day(dt):
    return get_first_day(dt, 0, 1) + timedelta(-1)


def to_human(date_):
    try:
        start = date_.split('-')[0]
        end = date_.split('-')[1]
        start_hours = start.split('.')[0]
        start_mins = start.split('.')[1]
        end_hours = end.split('.')[0]
        end_mins = end.split('.')[1]
        if int(start_mins) < 10:
            start_mins = "{}0".format(start_mins.rstrip())
        if int(end_mins) < 10:
            end_mins = "{}0".format(end_mins.rstrip())

        if int(start_hours) < 10:
            start_hours = "0{}".format(start_hours.lstrip())
        if int(end_hours) < 10:
            end_hours = "0{}".format(end_hours.lstrip())

        time_ = "{}:{} - {}:{}".format(start_hours, start_mins, end_hours, end_mins)
        return time_
    except:
        return ""
