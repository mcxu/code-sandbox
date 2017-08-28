package com;

public class TestMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CreditCard creditCard = new CreditCard();
		creditCard.setCardId(7);
		System.out.println("cardId=" + creditCard.getCardId());
	}

}

class CreditCard
{
	private int cardId = 9;
	public void setCardId(int cardID)
	{
		cardId = cardId;
	}
	public int getCardId()
	{
		return cardId;
	}
}
