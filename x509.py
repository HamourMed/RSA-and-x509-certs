from datetime import datetime, timedelta
from pyasn1.codec.der import encoder
from pyasn1.codec.der import decoder
from pyasn1.type import univ, namedtype, tag, constraint, char
from pyasn1_modules import rfc2459
import base64
from typing import Tuple, Callable
import rsa

name = Tuple[str, str, str, str, str, str]
date = Tuple[datetime, datetime]
Key = Tuple[int, int]


def generate_cert(serial_number : str, issuer_name : name, date : date, subject_name : name, pub_key : Key, prv_key : Key  ) :

    
    serial_number = int(serial_number, 16)

    issuer = rfc2459.Name()
    rdn_seq = rfc2459.RDNSequence()

    rdn1 = rfc2459.RelativeDistinguishedName()
    rdn1.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdn1.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_countryName)
    rdn1.getComponentByPosition(0).setComponentByName('value', char.PrintableString(issuer_name[0]))
    rdn_seq.setComponentByPosition(0, rdn1)

    rdn2 = rfc2459.RelativeDistinguishedName()
    rdn2.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdn2.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_stateOrProvinceName)
    rdn2.getComponentByPosition(0).setComponentByName('value', char.PrintableString(issuer_name[1]))
    rdn_seq.setComponentByPosition(1, rdn2)

    rdn3 = rfc2459.RelativeDistinguishedName()
    rdn3.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdn3.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_localityName)
    rdn3.getComponentByPosition(0).setComponentByName('value', char.PrintableString(issuer_name[2]))
    rdn_seq.setComponentByPosition(2, rdn3)

    rdn4 = rfc2459.RelativeDistinguishedName()
    rdn4.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdn4.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_organizationName)
    rdn4.getComponentByPosition(0).setComponentByName('value', char.PrintableString(issuer_name[3]))
    rdn_seq.setComponentByPosition(3, rdn4)

    rdn5 = rfc2459.RelativeDistinguishedName()
    rdn5.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdn5.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_organizationalUnitName)
    rdn5.getComponentByPosition(0).setComponentByName('value', char.PrintableString(issuer_name[4]))
    rdn_seq.setComponentByPosition(4, rdn5)

    rdn6 = rfc2459.RelativeDistinguishedName()
    rdn6.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdn6.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_commonName)
    rdn6.getComponentByPosition(0).setComponentByName('value', char.PrintableString(issuer_name[5]))
    rdn_seq.setComponentByPosition(5, rdn6)

    issuer=rdn_seq
    subject = rfc2459.Name()
    rdnn_seq = rfc2459.RDNSequence()

    rdnn1 = rfc2459.RelativeDistinguishedName()
    rdnn1.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdnn1.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_countryName)
    rdnn1.getComponentByPosition(0).setComponentByName('value', char.PrintableString(subject_name[0]))
    rdnn_seq.setComponentByPosition(0, rdnn1)

    rdnn2 = rfc2459.RelativeDistinguishedName()
    rdnn2.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdnn2.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_stateOrProvinceName)
    rdnn2.getComponentByPosition(0).setComponentByName('value', char.PrintableString(subject_name[1]))
    rdnn_seq.setComponentByPosition(1, rdnn2)

    rdnn3 = rfc2459.RelativeDistinguishedName()
    rdnn3.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdnn3.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_localityName)
    rdnn3.getComponentByPosition(0).setComponentByName('value', char.PrintableString(subject_name[2]))
    rdnn_seq.setComponentByPosition(2, rdnn3)

    rdnn4 = rfc2459.RelativeDistinguishedName()
    rdnn4.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdnn4.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_organizationName)
    rdnn4.getComponentByPosition(0).setComponentByName('value', char.PrintableString(subject_name[3]))
    rdnn_seq.setComponentByPosition(3, rdnn4)

    rdnn5 = rfc2459.RelativeDistinguishedName()
    rdnn5.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdnn5.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_organizationalUnitName)
    rdnn5.getComponentByPosition(0).setComponentByName('value', char.PrintableString(subject_name[4]))
    rdnn_seq.setComponentByPosition(4, rdnn5)

    rdnn6 = rfc2459.RelativeDistinguishedName()
    rdnn6.setComponentByPosition(0, rfc2459.AttributeTypeAndValue())
    rdnn6.getComponentByPosition(0).setComponentByName('type', rfc2459.id_at_commonName)
    rdnn6.getComponentByPosition(0).setComponentByName('value', char.PrintableString(subject_name[5]))
    rdnn_seq.setComponentByPosition(5, rdnn6)

    subject=rdnn_seq
    not_before = date[0]
    not_after = date[1]

    seq = univ.Sequence()
    for x in pub_key:
        seq.setComponentByPosition(len(seq), univ.Integer(x))
    der = encoder.encode(seq)

    pub_key_str = univ.BitString.fromOctetString(der)

    public_key_info = rfc2459.SubjectPublicKeyInfo()
    public_key_info.setComponentByName('algorithm', rfc2459.AlgorithmIdentifier())
    public_key_info.getComponentByName('algorithm').setComponentByName('algorithm', univ.ObjectIdentifier('1.2.840.113549.1.1.1')) # RSA encryption
    public_key_info.getComponentByName('algorithm').setComponentByName('parameters', univ.Null(''))
    public_key_info.setComponentByName('subjectPublicKey', pub_key_str)

    tbscertificate = rfc2459.TBSCertificate()
    tbscertificate.setComponentByName('version', rfc2459.Version('v1').subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    tbscertificate.setComponentByName('serialNumber', univ.Integer(serial_number))
    tbscertificate.setComponentByName('signature', rfc2459.AlgorithmIdentifier())
    tbscertificate.getComponentByName('signature').setComponentByName('algorithm', univ.ObjectIdentifier('1.2.840.113549.1.1.11')) # SHA256withRSA encryption
    tbscertificate.setComponentByName('issuer', issuer)
    tbscertificate.setComponentByName('validity', rfc2459.Validity())
    tbscertificate.getComponentByName('validity').setComponentByName('notBefore', rfc2459.Time())
    tbscertificate.getComponentByName('validity').getComponentByName('notBefore').setComponentByName('utcTime', not_before.strftime('%y%m%d%H%M%SZ'))
    tbscertificate.getComponentByName('validity').setComponentByName('notAfter', rfc2459.Time())
    tbscertificate.getComponentByName('validity').getComponentByName('notAfter').setComponentByName('utcTime', not_after.strftime('%y%m%d%H%M%SZ'))
    tbscertificate.setComponentByName('subject', subject)
    tbscertificate.setComponentByName('subjectPublicKeyInfo', public_key_info)

    der = encoder.encode(tbscertificate)
    cipher = rsa.sign_v1_5(der, private_key=prv_key, f_hash=rsa.sha256)
    signature = univ.BitString.fromOctetString(cipher)

    certificate = rfc2459.Certificate()
    certificate.setComponentByName('tbsCertificate', tbscertificate)
    certificate.setComponentByName('signatureAlgorithm', rfc2459.AlgorithmIdentifier())
    certificate.getComponentByName('signatureAlgorithm').setComponentByName('algorithm', univ.ObjectIdentifier('1.2.840.113549.1.1.11'))
    certificate.setComponentByName('signatureValue', signature)

    return certificate







def verifier_cert(certificate , certificate_ca ) -> bool :
    
    tbscert = certificate[0]
    signature = univ.BitString.asOctets(certificate[2])     

    
    tbscert_ca = certificate_ca[0]
    
    pub = univ.BitString.asOctets(tbscert_ca[5][1])

    seq = decoder.decode(pub)[0]
    pub = (int(seq[0]), int(seq[1]))


    return  rsa.verify_v1_5(signature, encoder.encode(tbscert), pub, rsa.sha256)

def save_cert(filename : str, certificate : rfc2459.Certificate) :

    template = '-----BEGIN CERTIFICATE-----\n{}\n-----END CERTIFICATE-----'    
    der = encoder.encode(certificate)
    res = template.format(base64.encodebytes(der).decode('ascii')) 
    with open(filename, 'w') as f:
        f.write(res)

def open_cert(filename : str) -> bytes:
    with open(filename, 'r') as f :
        pem = f.read()

    pem = pem.replace("\n",'').replace('-----BEGIN CERTIFICATE-----','').replace('-----END CERTIFICATE-----','').replace('\n','')
    res = base64.decodebytes(pem.encode('ascii'))   
    return (decoder.decode(res)[0])
    
