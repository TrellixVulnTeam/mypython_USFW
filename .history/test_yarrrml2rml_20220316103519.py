import subprocess
import unittest
import requests

# from yarrrml2rml import translate
# end-to-end test
class test_translate(unittest.TestCase):
    def test_convert_yarrrml2rml(self):
        # subprocess.Popen('translate_yarrrml2rml')
        
        yarrrml = open("./tests/yarrrml-input-test.yml").read()
        payload = {'yarrrml': yarrrml}
        rml_output = requests.post("http://127.0.0.1:5000/filermlconversion", payload)
        rml_output_path = open("./tests/rml-output-test.ttl", "w")
        rml_output_path.write(rml_output.text)

        try:
            expected_output = open("./tests/mapping-expected.rml.ttl").read()
            output = open("./tests/rml-output-test.ttl").read()
            rml_output_path.close()
            expected_output.close()
            output.close()
            self.assertEqual(expected_output, output)
            
        except Exception as e:
            print(str(e))
            results = "failed"
        
        

if __name__ == '__main__':
    unittest.main()