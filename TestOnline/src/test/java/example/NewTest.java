package example;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;

public class NewTest {
	private WebDriver driver;
  @Test
  public void f() 
  {
	  driver.get("http://store.demoqa.com/");
	  String atitle = driver.getTitle();
	  //System.out.println(atitle);
	  Assert.assertTrue(atitle.contains("ONLINE STORE | Toolsqa Dummy Test site"));
  }
  @BeforeTest
  public void beforeTest() 
  {
	  driver = new FirefoxDriver();
  }

  @AfterTest
  public void afterTest() 
  {
	  driver.quit();
  }

}
