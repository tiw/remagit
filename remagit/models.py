# -*- coding: utf-8 -*-
__author__ = 'wangting'

from enum import Enum


class Sku(object):
    def __init__(self, properties, quantity, price, outer_id):
        self._properties = properties
        self._quantity = quantity
        self._price = price
        self._outer_id = outer_id

    @property
    def properties(self):
        return self._properties

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self.price

    @property
    def outer_id(self):
        return self._outer_id


class Product(object):
    def __init__(self, price, title, desc, is_virtual, images, post_fee, skus):
        self._price = price
        self._title = title
        self._desc = desc
        self._is_virtual = is_virtual
        self._images = images
        self._post_fee = post_fee
        self._skus = skus

    @property
    def cid(self):
        return self._cid

    @property
    def promotion_cid(self):
        return self._promotion_cid

    @property
    def tag_ids(self):
        return self._tag_ids

    @property
    def price(self):
        return self._price

    @property
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc

    @property
    def is_virtual(self):
        return self._is_virtual

    @property
    def images(self):
        return self._images

    @property
    def post_fee(self):
        return self._post_fee

    @property
    def skus(self):
        return self._skus

    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, price):
        self._origin_price = price

    @property
    def buy_url(self):
        return self._buy_url

    @buy_url.setter
    def buy_url(self, url):
        self._buy_url = url

    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, id):
        self._outer_id = id

    @property
    def buy_quota(self):
        return self._buy_quota

    @buy_quota.setter
    def buy_quota(self, quota):
        self._buy_quota = quota

    @property
    def quantity(self):
        if len(self.skus > 0):
            quantity = 0
            for sku in self.skus:
                quantity += sku._quantity
            return quantity
        else:
            return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if len(self.skus) > 0:
            raise Exception('This product has sku, you cannot set quantity')
        else:
            self._quantity = quantity

    @property
    def hide_quantity(self):
        return self._hide_quantity

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        self.fields = fields


class User(object):
    def __init__(self, type, id, nick):
        self._type = type
        self._id = id
        self._nick = nick

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def nick(self):
        return self._nick


class Receiver(object):
    def __init__(self, city, district, name, state, address, zip, mobile):
        self.city = city
        self.name = name
        self.district = district
        self.state = state
        self.address = address
        self.zip = zip
        self.mobile = mobile


class Message(object):
    def __init(self, title, message):
        self.title = title
        self.message = message


class OrderItem(object):
    def __init__(self, num_iid, sku_id, num, outer_sku, outer_item_id, title, seller_nick, price, total_fee,
                 discount_fee, payment, sku_properties_name, messages):
        self.num_iid = num_iid
        self.sku_id = sku_id
        self.num = num
        self.outer_sku = outer_sku
        self.outer_item_id = outer_item_id
        self.title = title
        self.seller_nick = seller_nick
        self.price = price
        self.total_fee = total_fee
        self.discount_fee = discount_fee
        self.payment = payment
        self.sku_properties_name = sku_properties_name
        self.messages = messages


class FetchDetail(object):
    pass


class Coupon(object):
    pass


class Trade(object):
    def __init__(self, tid, num, num_iid, price, weixin_user_id, buyer, seller_flag, trade_memo, receiver, feedback,
                 outer_tid, status, shipping_type, post_fee, total_fee, discount_fee, payment, created_at, updated_at,
                 pay_time, pay_type, consign_time, sign_time, buyer_area, orders, fetch_detail, coupons, sub_trades):
        self.sub_trades = sub_trades
        self.coupons = coupons
        self.fetch_detail = fetch_detail
        self.orders = orders
        self.buyer_area = buyer_area
        self.sign_time = sign_time
        self.consign_time = consign_time
        self.pay_type = pay_type
        self.pay_time = pay_time
        self.updated_at = updated_at
        self.created_at = created_at
        self.payment = payment
        self.discount_fee = discount_fee
        self.total_fee = total_fee
        self.post_fee = post_fee
        self.shipping_type = shipping_type
        self.status = status
        self.outer_tid = outer_tid
        self.feedback = feedback
        self.receiver = receiver
        self.trade_memo = trade_memo
        self.seller_flag = seller_flag
        self.buyer = buyer
        self.price = price
        self.num_iid = num_iid
        self.num = num
        self.tid = tid
        self.weixin_user_id = weixin_user_id


class LogisticStatus(Enum):
# 在途，即货物处于运输过程中；
    on_road = 1
# 揽件，货物已由快递公司揽收并且产生了第一条跟踪信息；
    accepted = 2
# 疑难，货物寄送过程出了问题；
    interrupted = 3
# 签收，收件人已签收；
    assigned = 4
# 退签，即货物由于用户拒签、超区等原因退回，而且发件人已经签收；
    received = 5
# 派件，即快递正在进行同城派件；
    shipping = 6
# 退回，货物正处于退回发件人的途中；
    rejected = 7
# 转单
    transferred = 8


class LogisticTrace(object):
    def __init__(self, out_sid, company_name, tid, status):
        self.status = status
        self.tid = tid
        self.company_name = company_name
        self.out_sid = out_sid

