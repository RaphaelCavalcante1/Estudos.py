nm = str(input("\33[1;34;43mQual Carro Você Tem ? \33[m")).strip().upper()
if nm == 'MCLAREN':
    print('\33[1mCaraca, que carrão que você tem!')
elif nm in 'COROLA CORVETE DODGERAM PORSHE':
    print('\33[1mMeu deus, seu carro e dos bom !')
else:
    print('\33[1mVocê tem um carro padrão!')