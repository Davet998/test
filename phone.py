import phonenumbers
x = phonenumbers.parse("+442083661177", None)
print(x)
#Country Code: 44 National Number: 2083661177 Leading Zero: False
print(type(x))
y = phonenumbers.parse("020 8366 1177", "GB")
print(y)
z = phonenumbers.parse("00 1 650 253 2222", "GB")  # as dialled from GB, not a GB number
print(z)

z = phonenumbers.parse("+120012301", None)
print(z)

print(phonenumbers.is_possible_number(z))  # too few digits for USA
#False
z = phonenumbers.parse("+12001230101", None)
print(z)
print(phonenumbers.is_possible_number(z))
#True
print(phonenumbers.is_valid_number(z))  # NPA 200 not used
#False

text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    print(match)

#PhoneNumberMatch [11,23) 510-748-8230
#PhoneNumberMatch [51,62) 703-4800500
for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))

from phonenumbers import geocoder
ch_number = phonenumbers.parse("0431234567", "CH")
print(repr(geocoder.description_for_number(ch_number, "de")))

print(repr(geocoder.description_for_number(ch_number, "en")))

print(repr(geocoder.description_for_number(ch_number, "fr")))

print(repr(geocoder.description_for_number(ch_number, "it")))

from phonenumbers import carrier
uk_number = phonenumbers.parse("+40721234567", "RO")
print(repr(carrier.name_for_number(uk_number, "en")))

from phonenumbers import timezone
gb_number = phonenumbers.parse("+447986123456", "GB")
print(str(timezone.time_zones_for_number(gb_number)))
