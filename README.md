# BrightnessSpline ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ExtremeXT/BrightnessSpline/workflow.yml?branch=main&logo=github&style=for-the-badge)

Python script that generates an Android-compatible screen brightness map to be added in a DisplayConfig XML file from a framework-res overlay.

The BrightnessSpline project is licensed under the GNU Affero General Public License v3.0. See LICENSE for details.

## Usage

1. CD to the script folder
2. Install the required modules: ```pip install -r requirements.txt```
3. Move your overlay to `overlay.xml` in the same directory as the script
4. Configure the script's values
4. Run the script: ```python BrightnessSpline.py```
5. Create a DisplayConfig XML based on the output of the script
6. Enjoy!

Hint: use `pip3` and `python3` on Linux/macOS operating systems.

Here is an example of a script output: 
```
0.0, 0.0131, 0.0408, 0.1193, 0.3203, 0.4167, 0.4412, 0.5065, 0.7157, 1.0
2, 7.5, 26.3, 100, 355.7, 500, 527.4, 606, 857.7, 1200
```

And an example DisplayConfig screenBrightnessMap using those values:
```
    <screenBrightnessMap>
        <point>
            <value>0.0</value>
            <nits>2</nits>
        </point>
        <point>
            <value>0.0131</value>
            <nits>7.5</nits>
        </point>
        <point>
            <value>0.0408</value>
            <nits>26.3</nits>
        </point>
        <point>
            <value>0.1193</value>
            <nits>100</nits>
        </point>
        <point>
            <value>0.3203</value>
            <nits>355.7</nits>
        </point>
        <point>
            <value>0.4167</value>
            <nits>500</nits>
        </point>
        <point>
            <value>0.4412</value>
            <nits>527.4</nits>
        </point>
        <point>
            <value>0.5065</value>
            <nits>606</nits>
        </point>
        <point>
            <value>0.7157</value>
            <nits>857.7</nits>
        </point>
        <point>
            <value>1.0</value>
            <nits>1200</nits>
        </point>
    </screenBrightnessMap>
```
