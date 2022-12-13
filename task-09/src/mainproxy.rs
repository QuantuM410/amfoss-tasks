use self::csv::Writer;
use self::scraper::Selector;
use self::scraper::Html;

fn main() {

	let response = reqwest::blocking::get(
		"https://crypto.com/price"
	)
	.unwrap()
	.text()
	.unwrap();

	let document = scraper::Html::parse_document(&response);
	
	let price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
	let prices = document.select(&price_selector).map(|x| x.inner_html());
	println!("{}",prices)

	let name_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
	let names = document.select(&name_selector).map(|x| x.inner_html());

	let h24c_selector = scraper::Selector::parse("p.chakra-text.css-dg4gux").unwrap();
	let h24change = document.select(&h24c_selector).map(|x| x.inner_html());

	let h24v_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
	let h24volume = document.select(&h24v_selector).map(|x| x.inner_html());

	let marcap_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
	let marcap = document.select(&marcap_selector).map(|x| x.inner_html());

	let mut wtr = Writer::from_path("rustfile.csv");
	

	println!("Names");
	names
	.zip(1..51)
	.for_each(|(item, number)| println!("{}. {}", number, item)| wtr.write_record(&[item]));
	

	println!("Prices");
	prices
	.zip(1..51)
	.for_each(|(item, number)| println!("{}. {}", number, item)| wtr.write_record(&[item]));

	println!("24 Hour Change");
	
	h24change //gotta work here on tag ig
	.zip(1..101)
	.for_each(|(item, number)| println!("{}. {}", number, item)| wtr.write_record(&[item]));

	println!("24 Hour Volume");
	h24volume
	.zip(1..101)
	.for_each(|(item, number)| println!("{}. {}", number, item)| wtr.write_record(&[item]));

	println!("Market Cap");
	marcap
	.zip(1..101)
	.for_each(|(item, number)| println!("{}. {}", number, item)| wtr.write_record(&[item])); //tag marcap & h24volume same occur alternatively


}	
