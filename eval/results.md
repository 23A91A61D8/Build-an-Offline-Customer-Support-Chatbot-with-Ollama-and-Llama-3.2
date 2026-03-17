## Scoring Rubric

- Relevance (1-5): How well the response answers the customer query
- Coherence (1-5): Clarity and grammatical correctness of the response
- Helpfulness (1-5): How useful and actionable the response is

| Query # | Customer Query | Prompt Type | Response | Relevance | Coherence | Helpfulness |
|---------|----------------|-------------|----------|------------|------------|--------------|
| 1 | How can I track my order? | Zero-Shot | You can track your order by logging into your account on our website, clicking on 'Order History', and selecting the specific order you'd like to track. Alternatively, you can also use the tracking information provided in your order confirmation email to check on the status of your shipment with the shipping carrier. If you need further assistance, please let me know! | 5 | 5 | 5 |
| 1 | How can I track my order? | One-Shot | "Once you've received your order, you'll receive an email with tracking information. You can then use this to track the status of your package on the shipping carrier's website or through their mobile app." | 5 | 4 | 5 |
| 2 | My discount code is not working at checkout. | Zero-Shot | Sorry to hear that your discount code isn't working at checkout. Can you please provide me with the code and I'll check on it for you? Additionally, was this issue occurring after entering the code or immediately when trying to apply it during checkout? | 4 | 5 | 3 |
| 2 | My discount code is not working at checkout. | One-Shot | "I apologize that your discount code isn't working at checkout. Can you please provide me with the details of the code, such as its name or number, so I can assist you further?" | 4 | 5 | 5 |
| 3 | What is your return policy? | Zero-Shot | Our return policy at Chic Boutique is as follows:

If you're not completely satisfied with your purchase, you can initiate a return within 30 days of delivery. To start the process, please contact our customer service team via email or phone, and we'll provide you with a Return Merchandise Authorization (RMA) number.

Please ensure that the item(s) are in their original condition with all tags, packaging, and accessories included. We also require proof of purchase to facilitate the return.

Refunds will be processed within 5-7 business days of receiving the returned items. Please note that shipping costs for returns are the responsibility of the customer.

If you have any questions or concerns about our return policy, feel free to ask, and we'll do our best to assist you! | 5 | 5 | 5 |
| 3 | What is your return policy? | One-Shot | "I'm not sure about our current return policy, as it may have changed or I'm not up-to-date on the latest information. Can you please check our website or contact our customer service team directly for the most accurate and up-to-date information?" | 4 | 4 | 5 |
| 4 | How long does shipping take? | Zero-Shot | At Chic Boutique, we strive to get your orders to you as quickly as possible! Our standard shipping typically takes 3-7 business days within the continental United States. For Alaska and Hawaii, please allow 7-10 business days. International shipments may take 14-21 business days or longer, depending on customs clearance. If you need more information or have a specific delivery date request, feel free to ask and I'll do my best to assist! | 5 | 5 | 5 |
| 4 | How long does shipping take? | One-Shot | "Shipping typically takes 3-7 business days within the continental US, and 7-14 business days for international shipments. However, please note that delivery times can vary depending on your location and the carrier's services." | 4 | 4 | 3 |
| 5 | Can I cancel my order after placing it? | Zero-Shot | "I'd be happy to help with your query! Unfortunately, once an order has been placed and shipped, we are unable to cancel it. If you need to make changes or stop the order before it ships, please contact us as soon as possible, but we can't guarantee that we'll be able to make any changes. Would you like me to help with anything else?" | 5 | 3 | 4 |
| 5 | Can I cancel my order after placing it? | One-Shot | "I'm sorry to hear that you'd like to cancel your order. Unfortunately, we do not allow cancellations once an order has been processed and shipped. However, I can try to assist you with returning the items and provide a refund or store credit if possible." | 5 | 4 | 3 |
| 6 | I received a damaged product. What should I do? | Zero-Shot | Sorry to hear that you received a damaged product from us. Please let me assist you further.

To help resolve the issue, could you please provide me with your order number and a photo of the damaged item? This will allow me to look into this matter for you and provide the best possible solution. | 5 | 5 | 5 |
| 6 | I received a damaged product. What should I do? | One-Shot | "I'm so sorry to hear that you received a damaged product. Can you please contact our customer service team directly at [insert contact email or phone number]? We'll be happy to assist you with replacing the item, issuing a refund, or providing further guidance on how to proceed." | 5 | 4 | 4 |
| 7 | Do you offer cash on delivery? | Zero-Shot | I'm happy to help, but I think there may be some confusion - Chic Boutique is an online store and we do not currently offer cash on delivery as a payment option. We have a secure payment system in place that accepts various credit/debit cards and other online payment methods. Would you like me to explain our payment options further? | 5 | 5 | 5 |
| 7 | Do you offer cash on delivery? | One-Shot | "I'm sorry, we don't currently offer cash-on-delivery payment options at Chic Boutique. We do offer various secure payment methods for online transactions." | 4 | 4 | 4 |
| 8 | How can I change my delivery address? | Zero-Shot | To update your shipping address, please log in to your Chic Boutique account and navigate to the "Order History" or "Account" section. From there, click on "Update Address" next to your current order. Follow the prompts to enter your new shipping address, and we'll do our best to make the change for you! If you need assistance with this process, feel free to contact us, and I'd be happy to help. | 5 | 4 | 5 |
| 8 | How can I change my delivery address? | One-Shot | "Our website allows you to update your delivery address during the checkout process or after placing an order. To make changes, log in to your account, go to 'Order History', find the order with the incorrect address, and click on 'Edit Delivery Address'. You can also contact our customer service team for assistance with updating your address." | 3 | 2 | 5 |
| 9 | Why was my payment declined? | Zero-Shot | I'm so sorry to hear that your payment was declined!

Can you please tell me a bit more about what happened? Was this decline on our website, or did it occur while making a purchase from another online store?

Additionally, I'd like to know the type of payment method you were using (e.g. credit card, PayPal, etc.). This will help me investigate further and get back to you with any necessary information. | 5 | 4 | 2 |
| 9 | Why was my payment declined? | One-Shot | "Unfortunately, I'm not able to access real-time transaction information. However, I can suggest checking your bank statement or contacting your bank directly to see if there were any issues with the payment. If you'd like, I can also provide more general information about our payment processing policies." | 5 | 5 | 5 |
| 10 | Can I exchange an item instead of returning it? | Zero-Shot | We strive to provide a seamless shopping experience for our customers, but exchanging an item instead of returning it isn't possible at this time. If you'd like to discuss alternative options or receive more information on our return policy, please let me know and I'll do my best to assist you further! | 4 | 5 | 4 |
| 10 | Can I exchange an item instead of returning it? | One-Shot | "We do allow exchanges, but you'll need to initiate the exchange process within 30 days of delivery and ensure that the original item is returned in its original condition with tags still attached. Would you like me to guide you through the exchange process?" | 3 | 4 | 5 |
| 11 | How do I contact customer support? | Zero-Shot | You can reach us through our website's Contact Us page, where you can send a message to our support team or click on Live Chat (if available) for real-time assistance. If you prefer, you can also contact us via phone at [insert phone number] or email at [insert email address]. We're here to help and will respond as soon as possible! | 5 | 4 | 2 |
| 11 | How do I contact customer support? | One-Shot | You can contact our customer support team by sending an email to [support@chicboutique.com](mailto:support@chicboutique.com) or by filling out the contact form on our website's 'Help' page. We respond to all inquiries within 24-48 hours during business hours. | 5 | 4 | 3 |
| 12 | Do you provide international shipping? | Zero-Shot | Yes, we do offer international shipping options. Please visit our website and navigate to the "Shipping" section for a list of countries we ship to and estimated delivery times. If you have any further questions or need assistance with a specific order, feel free to contact us! | 5 | 4 | 2 |
| 12 | Do you provide international shipping? | One-Shot | "Yes, we do offer international shipping. However, please note that additional customs and handling fees may apply depending on the destination country. For more information on international shipping rates and delivery times, please visit our website or contact our customer service team." | 5 | 3 | 4 |
| 13 | How can I apply a coupon code? | Zero-Shot | To apply a coupon code, simply follow these steps:

1. Open your shopping cart and click on "Checkout".
2. Scroll down to the "Discount" section.
3. Click on the "Apply Coupon" button.
4. Enter your coupon code in the field provided.
5. Click "Apply" to see if the code is valid.

If you need help with entering a specific code, feel free to ask and I'll do my best to assist you! | 5 | 5 | 5 |
| 13 | How can I apply a coupon code? | One-Shot | "Great question! To apply a coupon code, simply go to the checkout page of your cart and look for the 'Apply Coupon' field. Enter the code exactly as it appears on the coupon details page on our website or in any email we sent you. Then click 'Apply' to see if the code is valid and get the updated discount." | 5 | 5 | 3 |
| 14 | What should I do if I received the wrong item? | Zero-Shot | "Don't worry, we apologize if you've received the wrong item. Please contact our customer support team at [support@chicboutique.com](mailto:support@chicboutique.com) or call us at 1-800-CICHBOUT (242-4288). We'll be happy to assist you with a return and exchange for the correct item, or provide a store credit/refund. Can you please provide your order number so we can look into this further?" | 5 | 4 | 4 |
| 14 | What should I do if I received the wrong item? | One-Shot | "If you've received the wrong item, please contact our customer service team immediately so we can assist you in resolving the issue. We'll provide a replacement with the correct item or offer a store credit or refund, whichever you prefer. Your order number and a photo of the incorrect item will help us process this quickly." | 5 | 4 | 4 |
| 15 | How do I reset my account password? | Zero-Shot | To reset your password, please follow these steps:

1. Go to our website and click on the 'Log in' button at the top right corner of the page.
2. Click on 'Forgot Password'.
3. Enter your email address associated with your Chic Boutique account, and then click 'Send Password Reset Link'.
4. Check your email inbox for a password reset link from us.
5. Click on the link to create a new password.

If you have any issues or concerns, feel free to ask, and I'll be happy to help further! | 5 | 5 | 3 |
| 15 | How do I reset my account password? | One-Shot | "Please click on the 'Forgot Password' link on our login page and follow the instructions to reset your password. If you need assistance, you can also contact our customer support team at [support email] or [support phone number]. We'll be happy to help you recover your account." | 4 | 3 | 5 |
| 16 | Can I order without creating an account? | Zero-Shot | "Hello! Yes, you can place an order on our website without creating an account. However, we do recommend registering for an account to enjoy exclusive benefits such as access to special promotions, faster checkout, and personalized recommendations. If you have any other questions or need assistance with placing your order, feel free to ask!" | 2 | 3 | 4 |
| 16 | Can I order without creating an account? | One-Shot | "Unfortunately, our website requires customers to create an account before checking out. However, you can still view our products and add items to your cart as a guest. To proceed with payment and checkout, please sign up for an account or contact us directly." | 5 | 4 | 3 |
| 17 | How do I check my order history? | Zero-Shot | You can easily view your order history by logging into your account on our website. To do this, follow these steps:

1. Go to our website and click on the "Login" button at the top right corner of the page.
2. Enter your email address and password in the login form.
3. Click on the "Account" dropdown menu and select "Order History".
4. You will see a list of all your past orders, including order details, shipping information, and status.

If you're having trouble logging in or accessing your order history, feel free to contact us at [support@chicboutique.com](mailto:support@chicboutique.com) and we'll be happy to help! | 4 | 5 | 3 |
| 17 | How do I check my order history? | One-Shot | "From our website, click on 'Account' at the top right corner and select 'Order History'. You'll be able to view all your past orders, including tracking information and details about any returns or exchanges you may have made. If you need help finding your order history, feel free to contact us and we'll be happy to assist you!" | 3 | 4 | 5 |
| 18 | Are there any additional delivery charges? | Zero-Shot | At Chic Boutique, we strive to keep our shipping costs as low as possible. There are no additional delivery charges for orders over $50. However, please note that we may charge a flat rate of $8 for international shipments. If your order is under $50, the shipping cost will be calculated based on the destination and weight of the package. | 5 | 4 | 3 |
| 18 | Are there any additional delivery charges? | One-Shot | "We do not charge additional delivery fees for domestic orders. However, international orders may incur an extra fee which is displayed at checkout. For more information on our shipping rates and policies, please visit our website or contact us directly." | 5 | 5 | 3 |
| 19 | What payment methods do you accept? | Zero-Shot | At Chic Boutique, we accept a variety of popular payment methods:

- Visa
- Mastercard
- American Express
- Discover
- PayPal
- Apple Pay (available on our mobile website)

Please note that availability may vary depending on your location. If you have any further questions or concerns about payment options, feel free to ask! | 5 | 4 | 3 |
| 19 | What payment methods do you accept? | One-Shot | "We currently accept Visa, Mastercard, American Express, and PayPal as payment methods on our website." | 4 | 5 | 4 |
| 20 | How can I get a refund for my order? | Zero-Shot | To initiate a refund, please contact our customer support team directly at [support@chicboutique.com](mailto:support@chicboutique.com) or call us at 1-800-CHIC-BOUT (1-800-242-4288). We'll be happy to guide you through the process and provide a refund if your order can be returned within our return window. Can I assist you further? | 5 | 5 | 3 |
| 20 | How can I get a refund for my order? | One-Shot | "I'm sorry to hear that you're experiencing issues with your order. To request a refund, please contact our customer service team via email or phone, and we'll guide you through the process of initiating a return. You can also start this process from your order history page once you've initiated contact with us." | 5 | 4 | 4 |
