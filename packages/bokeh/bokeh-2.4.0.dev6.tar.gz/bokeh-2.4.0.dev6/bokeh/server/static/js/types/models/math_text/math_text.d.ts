import * as p from "../../core/properties";
import * as visuals from "../../core/visuals";
import { Signal0 } from "../../core/signaling";
import { Context2d } from "../../core/util/canvas";
import { Model } from "../../model";
import { Size } from "../../core/types";
import { View } from "../../core/view";
import { RendererView } from "../renderers/renderer";
import { GraphicsBox, TextHeightMetric, Position } from "../../core/graphics";
import { Rect } from "../../core/util/affine";
import { BBox } from "../../core/util/bbox";
declare type MathJaxStatus = "not_started" | "loaded" | "loading" | "failed";
export declare abstract class MathJaxProvider {
    readonly ready: Signal0<this>;
    status: MathJaxStatus;
    abstract get MathJax(): typeof MathJax | null;
    abstract fetch(): Promise<void>;
}
export declare class NoProvider extends MathJaxProvider {
    get MathJax(): null;
    fetch(): Promise<void>;
}
export declare class CDNProvider extends MathJaxProvider {
    get MathJax(): typeof MathJax | null;
    fetch(): Promise<void>;
}
export declare class BundleProvider extends MathJaxProvider {
    _mathjax: typeof MathJax | null;
    get MathJax(): typeof MathJax | null;
    fetch(): Promise<void>;
}
/**
 * Helper class to rendering MathText into Canvas
 */
export declare class MathTextView extends View implements GraphicsBox {
    model: MathText;
    parent: RendererView;
    angle?: number;
    _position: Position;
    align: "left" | "center" | "right" | "justify";
    infer_text_height(): TextHeightMetric;
    _base_font_size: number;
    set base_font_size(v: number | null | undefined);
    get base_font_size(): number;
    font_size_scale: number;
    private font;
    private color;
    private svg_image;
    private svg_element;
    get has_image_loaded(): boolean;
    _rect(): Rect;
    set position(p: Position);
    get position(): Position;
    get text(): string;
    get provider(): MathJaxProvider;
    lazy_initialize(): Promise<void>;
    connect_signals(): void;
    set visuals(v: visuals.Text);
    /**
     * Calculates position of element after considering
     * anchor and dimensions
     */
    protected _computed_position(): {
        x: number;
        y: number;
    };
    /**
     * Uses the width, height and given angle to calculate the size
    */
    size(): Size;
    private get_text_dimensions;
    private get_image_dimensions;
    _size(): Size;
    bbox(): BBox;
    rect(): Rect;
    paint_rect(ctx: Context2d): void;
    paint_bbox(ctx: Context2d): void;
    /**
     * Render text into a SVG with MathJax and load it into memory.
     */
    private load_image;
    /**
     * Takes a Canvas' Context2d and if the image has already
     * been loaded draws the image in it otherwise draws the model's text.
    */
    paint(ctx: Context2d): void;
}
export declare namespace MathText {
    type Attrs = p.AttrsOf<Props>;
    type Props = Model.Props & {
        text: p.Property<string>;
    };
}
export interface MathText extends MathText.Attrs {
}
export declare class MathText extends Model {
    properties: MathText.Props;
    __view_type__: MathTextView;
    constructor(attrs?: Partial<MathText.Attrs>);
}
export {};
//# sourceMappingURL=math_text.d.ts.map