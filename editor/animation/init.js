//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210', 'snap.svg_030'],
    function (ext, $, Raphael, Snap) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide = {};
            cur_slide["in"] = data[0];
            this_e.addAnimationSlide(cur_slide);
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            //YOUR FUNCTION NAME
            var fname = 'draw';

            var checkioInput = data.in;
            var checkioInputStr = fname + '(' +
                JSON.stringify(checkioInput).replace(/\[/g, "(").replace(/]/g, ")").replace("((", "{(").replace("))", ")}")
                + ')';

            var failError = function (dError) {
                $content.find('.call').html(checkioInputStr);
                $content.find('.output').html(dError.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
            };

            if (data.error) {
                failError(data.error);
                return false;
            }

            if (data.ext && data.ext.inspector_fail) {
                failError(data.ext.inspector_result_addon);
                return false;
            }

            $content.find('.call').html(checkioInputStr);
            $content.find('.output').html('Working...');

            var svg = new ExpDraw($content.find(".explanation svg")[0]);
            svg.prepare(checkioInput);


            if (data.ext) {
                var rightResult = data.ext["answer"];
                var userData = data.out;
                var userResult = userData[0];
                var userResultStr = userData[1];
                var result = data.ext["result"];
                var result_addon = data.ext["result_addon"];
                var result_message = result_addon[1];
                var result_show = result_addon[0];

                //if you need additional info from tests (if exists)
                var explanation = data.ext["explanation"];
                $content.find('.output').html('&nbsp;Your result:&nbsp;' + userResultStr);
                if (!result) {
                    $content.find('.answer').html(result_message);
                    $content.find('.answer').addClass('error');
                    $content.find('.output').addClass('error');
                    $content.find('.call').addClass('error');
                }
                if (result_show) {
                    svg.animateLines(userResult);
                }
            }
            else {
                $content.find('.answer').remove();
            }


            //Your code here about test explanation animation
            //$content.find(".explanation").html("Something text for example");
            //
            //
            //
            //
            //


            this_e.setAnimationHeight($content.height() + 60);

        });

        //This is for Tryit (but not necessary)
//        var $tryit;
//        ext.set_console_process_ret(function (this_e, ret) {
//            $tryit.find(".checkio-result").html("Result<br>" + ret);
//        });
//
//        ext.set_generate_animation_panel(function (this_e) {
//            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit'))).find('.tryit-content');
//            $tryit.find('.bn-check').click(function (e) {
//                e.preventDefault();
//                this_e.sendToConsoleCheckiO("something");
//            });
//        });
        function ExpDraw(dom) {
            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var p = 20;

            var minX = Infinity,
                minY = Infinity,
                maxX = 0,
                maxY = 0;

            var cell;

            var paper;

            var sizeX = 380;
            var sizeY = 380;

            var attrShadow = {stroke: colorGrey4, strokeWidth: 5, strokeLinecap: "round"};
            var attrLine = {stroke: colorBlue4, strokeWidth: 2, strokeLinecap: "round"};

            this.prepare = function (lines) {
                for (var i = 0; i < lines.length; i++) {
                    var line = lines[i];
                    minX = Math.min(minX, line[0], line[2]);
                    maxX = Math.max(maxX, line[0], line[2]);
                    minY = Math.min(minY, line[1], line[3]);
                    maxY = Math.max(maxY, line[1], line[3]);
                }
                var diff = Math.max(maxY - minY, maxX - minX);
                cell = (sizeX - 2 * p) / diff;
                paper = Snap(dom);
                sizeY = p * 2 + cell * (maxY - minY);
                paper.attr({width: sizeX, height: sizeY});

                for (i = 0; i < lines.length; i++) {
                    var segm = lines[i];
                    paper.line(
                        (segm[0] - minX) * cell + p,
                        sizeY - (segm[1] - minY) * cell - p,
                        (segm[2] - minX) * cell + p,
                        sizeY - (segm[3] - minY) * cell - p).attr(attrShadow);
                }

            };

            this.animateLines = function (points) {
                var count = 0;
                var stepTime = 2;
                (function draw() {
                    if (count >= points.length - 1) {
                        return false;
                    }
                    var f = points[count];
                    var s = points[count + 1];
                    var segm = paper.path(Snap.format(
                        "M{f0},{f1}L{f0},{f1}",
                        {
                            f0: (f[0] - minX) * cell + p,
                            f1: sizeY - (f[1] - minY) * cell - p})).attr(attrLine);
                var dist = Math.sqrt(Math.pow(f[0] - s[0], 2) + Math.pow(f[1] - s[1], 2)) * cell;
                segm.animate(
                    {"path": Snap.format("M{f0},{f1}L{s0},{s1}",
                        {
                            f0: (f[0] - minX) * cell + p,
                            f1: sizeY - (f[1] - minY) * cell - p,
                            s0: (s[0] - minX) * cell + p,
                            s1: sizeY - (s[1] - minY) * cell - p})}, dist * stepTime,
                    callback = function(){count++; draw()});

            }()
        )
            ;
        }
    }

}
)
;
